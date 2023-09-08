#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Annotated
from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt

from config import Informations
from components.Passwords import Passwords
from utilities.DBConnections import DBManager

passwordsClass = Passwords()
db = DBManager()


class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AuthManager:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self) -> None:
        pass

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_user(self, email: str):
        user = db.query(f"SELECT * FROM `users` WHERE `email`='{email}'")
        if user:
            return user

    def authenticate_user(self, email: str, password: str):
        user = self.get_user(email)
        if not user:
            return False
        if not self.verify_password(password, user[0]["password"]):
            return False
        return user

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, Informations.SECRET_KEY.value, algorithm=Informations.ALGORITHM.value)
        return encoded_jwt
    
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    auth = AuthManager()
    user = auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=Informations.ACCESS_TOKEN_EXPIRE_MINUTES.value)
    access_token = auth.create_access_token(
        data={"sub": user[0]["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/password/search/")
async def searchpass(token: Annotated[str, Depends(oauth2_scheme)], query: str = ""):
    auth = AuthManager()
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, Informations.SECRET_KEY.value, algorithms=[Informations.ALGORITHM.value])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = auth.get_user(email=token_data.username)
    if user is None:
        raise credentials_exception
    
    return passwordsClass.search_pwd(query)

# auth = AuthManager()
# print(auth.create_access_token({"sub": "sidotidavide@gmail.com"}))
