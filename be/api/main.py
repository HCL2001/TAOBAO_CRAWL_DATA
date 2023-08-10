from fastapi import Depends, FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
import crud
import models
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session

from datetime import datetime
import jwt
from security import verify_password, generate_token, validate_token, check_token_expired


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
    return await crud.crawl_taobao(keyWord)

@app.post('/expired/')
def check_token_expire(check_token: schemas.CheckToken):
    return check_token_expired(check_token.token)

@app.get("/list")
async def get_list(page_number: int = 1, items_per_page: int = 10):
    return crud.get_data_from_db(page_number, items_per_page)

@app.get("/detail")
def get_detail(id):
    return crud.detailV2(id)

@app.get("/patternDetail", dependencies=[Depends(validate_token)])
def pattern_Detail():
    return crud.patternForDetailV2()

@app.get("/test_get_detail")
def test_get_detail(product_url):
    return crud.get_product_detail(product_url)

@app.get("/detailV2")
def get_detailV2(id):
    return crud.detailV2(id)

@app.delete("/", dependencies=[Depends(validate_token)])
def deleteById(id):
    return crud.deleteById(id)

@app.post("/cart", )
def add_to_cart(request_data: schemas.CartItem):
    return crud.add_to_cart(request_data)

@app.get("/cart", dependencies=[Depends(validate_token)])
def get_cart(username: str):
    return crud.get_cart_with_items(username)