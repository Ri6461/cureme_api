from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db, secret, SessionLocal
from jose import jwt
from jose.exceptions import JWTError
# from ..app import USER, get_current_active_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class USER(schemas.BaseModel):
    id: int
    sub: str
    nam: str | None = None
    pic: str | None = None
    disabled: bool = False

class TokenData(schemas.BaseModel):
    username: str | None = None

def get_user(username: str):
    return crud.get_user_by_email(db=SessionLocal(), email=username)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        username: str = payload.get("sub")
        ''' 
        if payload.get("disabled"):
            raise credentials_exception
        '''
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    payload['nam'] = payload['name']
    payload.pop('name')
    return USER(id=payload['id'], sub=payload['sub'], pic=payload['pic'], nam=payload['nam'], disabled=False)

async def get_current_active_user(
    current_user: Annotated[USER, Depends(get_current_user)],
):
    '''
    if not current_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    '''
    return current_user

router = APIRouter()

@router.get("/user", response_model=List[schemas.Notification])
def read_notification(current_user: Annotated[USER, Depends(get_current_active_user)], db: Session = Depends(get_db)):
    '''
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    '''
    db_notification = crud.get_notification_by_email(db, email=current_user.sub)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="No Notifications found for this user.")
    return db_notification

@router.get("/", response_model=list[schemas.Notification])
def read_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notifications = crud.get_notifications(db, skip=skip, limit=limit)
    return notifications

@router.put("/", response_model=schemas.Notification)
def create_notification(notification: schemas.NotificationCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_notification(db=db, notification=notification, user_id=user_id)

@router.patch("/{notification_id}", response_model=schemas.Notification)
def update_notification(notification_id: int, notification: schemas.NotificationUpdate, db: Session = Depends(get_db)):
    db_notification = crud._get_notification(db, notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return crud.update_notification(db=db, notification_id=notification_id, notification=notification)

@router.delete("/{notification_id}", response_model=schemas.Notification)
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    db_notification = crud._get_notification(db, notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return crud.delete_notification(db=db, notification_id=notification_id)
