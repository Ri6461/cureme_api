from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db, digest, secret
from jose import jwt


router = APIRouter()

@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.put("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db), hashed: bool = False):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    if not hashed:
        user.secret = digest(user.secret)
    return crud.create_user(db=db, user=user)


@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    payload = {
        'id': db_user.id,
        'username': db_user.username,
        'email': db_user.email,
        'avatar': db_user.avatar,
        'name': db_user.first_name + ' ' + db_user.last_name,
    }
    if digest(user.secret) == db_user.secret:
        token = jwt.encode(payload, secret, algorithm='HS256')
        return {"jwt": token}
    raise HTTPException(status_codes=401, detail="Invalid credentials supplied.")


@router.post("/auth")
def auth(creds: schemas.UserAuth):
    data = jwt.decode(creds.token, secret, algorithms=['HS256'])
    if data:
        return data
    raise HTTPException(status_codes=401, detail="Invalid credentials supplied.")


@router.patch("/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user_id=user_id, user=user)

@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)
