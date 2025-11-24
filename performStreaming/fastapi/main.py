
from typing import TypedDict
from fastapi import FastAPI
from enum import Enum

from pydantic import BaseModel

app = FastAPI()



@app.get('/')
async def root():
    return {"message": "success"}


@app.get('/items/{item_id}')
async def read_item(item_id):
    return {"item_id": item_id}


class ModelEnum(str, Enum):
        alexnet = "alexnet"
        resnet = "resnet"
        lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelEnum):
    if model_name is ModelEnum.alexnet:
        return {"model_name": model_name, "message": "Deep learning FTW"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}    



@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {"file_path": file_path}


# 查询参数


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# 多个路径和查询参数, 声明查询参数的顺序并不重要。

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
    q: str | None = None,
    short: bool | None = None
):
 item = {"item_id": item_id, "owner_id": user_id}

 if q:
    item.update({"q": q})
 if not short:
    item.update(
        {"description": "This is an amzaing item has a long description"}
    )
 return item   



 # 请求体
 from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class ItemDict(TypedDict):
    id: int
    name: str
    optional_field: str | None



@app.post('/items')
async def create_item(item: Item):
  item_dict = item.model_dump()

  if item.tax is not None:
     price_with_tax = item.price + item.tax
     item_dict.update({"price_with_tax": price_with_tax})

  return item_dict   



# FastAPI 能识别与路径参数匹配的函数参数，
# 还能识别从请求体中获取的类型为 Pydantic 模型的函数参数

@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
      result.update({"q": q})  
    return result