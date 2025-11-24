from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()

class UserBase(BaseModel):
     username: str
     email: EmailStr
     full_name: str | None = None

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
     pass

class UserInDB(UserBase):
    hashed_password: str      

def fake_password_hasher(raw_psd: str):
     return "superuser" + raw_psd


def fake_save_user(user: UserIn):
     hash_psd = fake_password_hasher(user.password)
     user_in_db = UserInDB(**user.model_dump(), hashed_password=hash_psd)
     print("User" + user_in_db)
     return user_in_db

@app.post("/user", response_model=UserOut)
async def create_user(user: UserIn):
    user_save =  fake_save_user(user)   
    return user_save 