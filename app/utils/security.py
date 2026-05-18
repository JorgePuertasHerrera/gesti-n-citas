import bcrypt
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.db.database import get_db
from app.models.user import User
from datetime import datetime, timedelta, timezone

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

SECRET_KEY = "tuclaveSecreta"
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
def verify_password(plain_password: str, hashed_password:str)-> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"),hashed_password.encode("utf-8"))
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = 30)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
def get_current_user(token: str = Depends(oauth2_scheme), db= Depends(get_db)):
    credentials_exception = HTTPException(status_code=401, detail="No autorized")
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception
    return user