from datetime import datetime, timedelta
from typing import Union, Any

import crud
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from passlib.context import CryptContext
from pydantic import ValidationError

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def check_password_hash(password, account_pass):
    return pwd_context.verify(password, account_pass)


def verify_password(username, password, db):
    try:
        account = crud.get_user_by_username(db, username).first()
        check_pass = check_password_hash(password, account.password)
        if account and check_pass:
            return True
        else:
            return False
    except Exception as e:
        return {
            'status': 'failed',
            'message': str(e)
        }
    finally:
        db.close()


def generate_token(username: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
    )
    to_encode = {
        "exp": expire, "username": username
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    return encoded_jwt


def check_token_expired(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[SECURITY_ALGORITHM])
        expiration_time = datetime.fromtimestamp(payload["exp"])
        if expiration_time < datetime.now():
            return False
        return True
    except(jwt.PyJWTError, ValidationError):
        return False


def validate_token(http_authorization_credentials=Depends(reusable_oauth2)) -> str:
    try:
        payload = jwt.decode(http_authorization_credentials.credentials, SECRET_KEY, algorithms=[SECURITY_ALGORITHM])
        expiration_time = datetime.fromtimestamp(payload["exp"])
        if expiration_time < datetime.now():
            raise HTTPException(status_code=403, detail="Token expired")
        return payload.get('username')
    except(jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=403,
            detail=f"Could not validate credentials",
        )
