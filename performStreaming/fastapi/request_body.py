from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: Annotated[int, Body()]):
    # importance: Annotated(int, Body()) 设置的意义是，告诉fastapi importance也是body的一员，而不是查询参数
    # 因为如果写为 importance: int  他就会和item_id 一样被放在查询参数集合里， 而不是和 item,user 一起放在body
    results = {"item_id": item_id, "item": item, "user": user}

    return results


# 带有 Pydantic 模型的 Cookie
from fastapi import Cookie, Header

class Cookies(BaseModel):
    model_config = {"extra": "forbid"} # 禁止（ forbid ）任何额外（ extra ）字段
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str  | None = None


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []

@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()], headers: Annotated[CommonHeaders, Header()]):
    return cookies
