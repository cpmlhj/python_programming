"""
  让我们假设你有一个数据库名为fake_db，它只能接收与JSON兼容的数据。

  例如，它不接收datetime这类的对象，因为这些对象与JSON不兼容。

  因此，datetime对象必须将转换为包含ISO格式化的str类型对象。

  同样，这个数据库也不会接收Pydantic模型（带有属性的对象），而只接收dict。

  对此你可以使用jsonable_encoder。

  它接收一个对象，比如Pydantic模型，并会返回一个JSON兼容的版本
"""

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from pydantic import BaseModel


fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()

@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data