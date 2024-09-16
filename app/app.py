#!/usr/bin/env python3

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from sqlalchemy.orm import Session
from .routers import users, medications, appointments, procedures, reminders, notifications, contacts, allergies, medical_conditions, labs, vaccines
from .database import init_db, get_db, SessionLocal, digest  # , engine
from .database import secret as jwt_secret
from . import crud, models, schemas
import requests
from jose import jwt
from jose.exceptions import JWTError
from os import environ as env
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from typing import Annotated


load_dotenv()
origins = ["*"]
# Initialize database.
init_db()
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
GOOGLE_CLIENT_ID = env.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = env.get('GOOGLE_CLIENT_SECRET')
GOOGLE_REDIRECT_URI = env.get('GOOGLE_REDIRECT_URI')


description = """
CureMe Medial App's REST API helps you do awesome stuff. 🚀

## Users

You will be able to:

* **Create users**
* **Read users**
* **Read user**
* **Update user**
* **Delete user**

<h3>
<blockquote><i> And so on.. </i></blockquote>
</h3>
"""


tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also supposed to be implemented here.",
    },
    {
        "name": "medications",
        "description": "Operations with medications.",
    },
    {
        "name": "appointments",
        "description": "Operations with appointments.",
    },
    {
        "name": "reminders",
        "description": "Operations with reminders.",
    },
    {
        "name": "notifications",
        "description": "Operations with notifications",
    },
    {
        "name": "contacts",
        "description": "Operations with contacts.",
    },
    {
        "name": "procedures",
        "description": "Operations with procedures.",
    },
    {
        "name": "allergies",
        "description": "Operations with allergies.",
    },
    {
        "name": "medical_conditions",
        "description": "Operations with medical_conditions.",
    },
    {
        "name": "labs",
        "description": "Labs operations with users.",
    },
    {
        "name": "vaccines",
        "description": "Labs operations with vaccines.",
    },
    {
        "name": "others",
        "description": "Manage others. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]; api = FastAPI(
    title="CureMe API",
    description=description,
    summary='CureMe Medical App\'s REST API.',
    version="0.0.2",
    terms_of_service="#",
    contact={
        "name": "profxadke",
        "url": "http://is.gd/nikhila",
        "email": "xadkeg@duck.com",
    },
    license_info={
        "name": "GNU General Public License v3 (GPL-3)",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
    openapi_tags=tags_metadata,
    docs_url=None, redoc_url=None
); app = api
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def custom_openapi():
    if api.openapi_schema:
        return api.openapi_schema
    openapi_schema = get_openapi(
        title="CureMe Medial App's REST API",
        version="0.0.1",
        summary="CureMe Medical App's REST API.",
        description=description,
        routes=api.routes,
        terms_of_service="#",
        contact={
            "name": "profxadke",
            "url": "http://is.gd/nikhila",
            "email": "xadkeg@duck.com",
        },
        license_info={
            "name": "GNU General Public License v3 (GPL-3)",
            "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
        }
    ); openapi_schema["info"]["x-logo"] = {
        "url": "http://127.0.0.1:8888/static/cureme.png"
    }; api.openapi_schema = openapi_schema
    openapi_schema['tags'] = tags_metadata
    return api.openapi_schema


api.openapi = custom_openapi


class Token(schemas.BaseModel):
    access_token: str
    token_type: str

class TokenData(schemas.BaseModel):
    username: str | None = None

class USER(schemas.BaseModel):
    id: int
    sub: str
    nam: str | None = None
    pic: str | None = None
    disabled: bool = False

class UserInDB(USER):
    hashed_passwd: str

def verify_password(plain_password, hashed_password):
    if digest(plain_password) == hashed_password:
        return True

def get_password_hash(password: str):
    return digest(password)

def get_user(username: str):
    return crud.get_user_by_email(db=SessionLocal(), email=username)

def authenticate_user(username: str, password: str):
    db_user = get_user(username)
    if not db_user:
        return False
    if password.lower().strip() in ('oauth', 'google', 'passswordless', 'passwdless'):
        oauth_secret = db_user.secret.split(':')[1]
        # TODO: IDK DO SOME VALIDATION HERE
        if oauth_secret:
            return db_user
        return False
    if verify_password(password, db_user.secret):
        return db_user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, jwt_secret, algorithm='HS256')
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, jwt_secret, algorithms=['HS256'])
        username: str = payload.get("sub")
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    payload['nam'] = payload['name']
    return dict(payload)

async def get_current_active_user(
    current_user: Annotated[USER, Depends(get_current_user)],
):
    return current_user

@api.post("/token", tags=['others'])
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"id": user.id, "sub": user.username, "pic": user.avatar, "name": user.first_name + ' ' + user.last_name}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@api.get("/me", response_model=USER, include_in_schema=False)
async def read_users_me(
    current_user: Annotated[USER, Depends(get_current_active_user)],
):
    return current_user


# Include routers
api.include_router(users.router, prefix="/users", tags=["users"])
api.include_router(medications.router, prefix="/medications", tags=["medications"])
api.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
api.include_router(reminders.router, prefix="/reminders", tags=["reminders"])
api.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
api.include_router(vaccines.router, prefix="/vaccines", tags=["vaccines"])
api.include_router(contacts.router, prefix="/contacts", tags=["contacts"])
api.include_router(procedures.router, prefix="/procedures", tags=["procedures"])
api.include_router(allergies.router, prefix="/allergies", tags=["allergies"])
api.include_router(medical_conditions.router, prefix="/medical_conditions", tags=["medical_conditions"])
api.include_router(labs.router, prefix="/labs", tags=["labs"])


@api.get("/", include_in_schema=False)
def redirect_docs(code: str = '', scope: str = '', authuser: int = 0, prompt: str = ''):
    if code:
        print(code, scope, authuser, prompt)
        phone, dob, addr = '+977 9847078791', '2011-11-11', 'Somewhere near your heart.'
        # TODO: DoNot-Hardcode [phone, dob, addr] like vars above.
        return RedirectResponse(f'/auth/google?code={code}&dob={dob}&phone={phone}&addr={addr}')
    return RedirectResponse(url="/docs/")


@api.get("/favicon.ico", include_in_schema=False)
def respond_favicon():
    return FileResponse("./app/static/favicon.ico")


@api.get("/favicon.png", include_in_schema=False)
def respond_favicon_png():
    return FileResponse("./app/static/favicon.png")


@api.get("/docs", include_in_schema=False)
def overridden_swagger():
	return get_swagger_ui_html(openapi_url="/openapi.json", title="CureMe API - Docs", swagger_favicon_url="/favicon.ico")


@api.get("/redoc", include_in_schema=False)
def overridden_redoc():
	return get_redoc_html(openapi_url="/openapi.json", title="CureMe API - ReDoc", redoc_favicon_url="/favicon.ico")


@api.get("/ping")
def pong():
    return {"ping": "pong!"}

@api.get("/login/google")
async def login_google():
    return RedirectResponse(f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline")

@api.get("/auth/google")
async def auth_google(code: str = '', dob: str = '', phone: str = '', addr: str = '', db: Session = Depends(get_db)):
    if not code:
        return RedirectResponse('/login/google')
    token_url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get("access_token")
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
    data = user_info.json()
    data['code'] = code
    if 'email' not in data:
        raise HTTPException(status_code=422, detail="No email supplied / provided in data.")
    # Check if user's email address is already registered.
    db_user = crud.get_user_by_email(db, email=data['email'])
    if db_user is None:
         phone_number = phone
         address = addr
         secret = f"oauth_{data['id']}:{data['code']}"
         updated_at = str(datetime.now()).replace(' ', 'T')[:23] + 'Z'
         created_at = updated_at
         username = data['email']
         db_user = models.User(
             email=data['email'],
             secret=secret,
             username=username,
             first_name=data['given_name'],
             last_name=data['family_name'],
             dob=dob,
             avatar=data['picture'],
             phone_number=phone_number,
             address=address,
             created_at=created_at,
             updated_at=updated_at
         )
         db.add(db_user)
         db.commit()
         db.refresh(db_user)
         db_user = crud.get_user_by_email(db, email=data['email'])
    payload = {
        'id': db_user.id,
        'username': db_user.username,
        'email': data['email'],
        'avatar': data['picture'],
        'name': db_user.first_name + ' ' + db_user.last_name
    }
    token = jwt.encode(payload, jwt_secret, algorithm='HS256')
    return {'token': token}


@api.get("/token", tags=['others'])
async def decode_token(token: str = Depends(oauth2_scheme)):
    try:
        return jwt.decode(token, GOOGLE_CLIENT_SECRET, algorithms=["HS256"])
    except JWTError:
        return HTTPException(status_code=401, detail="Invalid token supplied.")


api.mount("/static", StaticFiles(directory="./app/static"), name="static")


if __name__ == "__main__":
    __import__('uvicorn').run('app:api', host="0.0.0.0", port=8888, reload=False)