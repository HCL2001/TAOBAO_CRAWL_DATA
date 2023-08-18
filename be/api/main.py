from fastapi import Depends, FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
import crud
import models
import config
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session

import subprocess
from datetime import datetime
from typing import Optional
import jwt
# from croniter import croniter
# from crontab import CronTab
from security import verify_password, generate_token, validate_token, check_token_expired
from googletrans import *


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "https://reactjs-megasop.vercel.app",
    "https://react.thanhdev.info"
]

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/login')
def login(request_data: schemas.LoginRequest, db: Session = Depends(get_db)):
    print(f'[x] request_data: {request_data.__dict__}')
    if verify_password(username=request_data.username, password=request_data.password, db=db):
        token = generate_token(request_data.username)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[SECURITY_ALGORITHM])
        expiration_time = datetime.fromtimestamp(payload["exp"])
        return {
            'token': token,
            'expiration_time': expiration_time
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/taobao/{keyWord}", dependencies=[Depends(validate_token)])
async def search_taobao(keyWord: str):
    return await  crud.crawl_taobao(keyWord)
@app.post("/login_taobao")
def login_taobao_api():
    try:
        username = "0084818822357"
        password = "Aa@123123"
        url = "https://login.taobao.com/"
        crud.startBot(username, password, url)  # Gọi hàm startBot từ module crud
        return {"message": "Login and startBot successful"}
    except Exception as e:
        return {"message": "Login or startBot failed", "error": str(e)}



@app.post('/expired/')
def check_token_expire(check_token: schemas.CheckToken):
    return check_token_expired(check_token.token)

@app.get("/list")
async def get_list(page_number: int = 1, items_per_page: int = 10):
    return crud.get_data_from_db(page_number, items_per_page)


@app.get("/detail/{id}")
def get_detail(id : int):
    if id is None:
        return "id is null"
    return crud.get_detail_from_db(id)

@app.get("/demo")
def test_function():
    return crud.demo_function()

@app.get("/patternDetail")
def pattern_Detail():
    return crud.patternForDetail()


