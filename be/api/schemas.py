from pydantic import BaseModel

class SearchProduct(BaseModel):
    id: int
    name: str
    price: str
    link: str

    class Config:
        orm_mode = True
# class Detail(BaseModel):
#     id: int
#     name: str
#     price: str
#     link: str
#     promotion: str
#
#     class Config:
#         orm_mode = True
# Login ___________________________________________________________________________
class LoginRequest(BaseModel):
    username: str
    password: str


class CheckToken(BaseModel):
    token: str


class Setting(BaseModel):
    name: str
    quantity: int
    unit: str
    status: str