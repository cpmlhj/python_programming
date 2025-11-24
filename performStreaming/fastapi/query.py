from fastapi import FastAPI, Query
from typing import Union, List

app = FastAPI()

# 添加约束条件
# 你可以声明一个参数可以接收None值，但它仍然是必需的。这将强制客户端发送一个值，即使该值是None    
@app.get("/items/")
async def read_items(q: Union[str, None] = Query(max_length=50, min_length=5)): # 当Query 没有设置默认值时候，定为必填
    results = {
        "items": [
            {"item_id":  "Foo"},
            {"item_id": "Bar"}
        ]
    }

    if q:
        results.update({"q": q})
    return results

# /items_1?q=bar&q=foo&q=others
@app.get("/items_1/")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q" : q }
    return query_items


#  路径参数和数值校验

from typing import Annotated
from fastapi import Path


@app.get("/items_2/{item_id}")
async def path_read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get ")],
    q: Annotated[str | None, Query(alias="item-query")] = None
):
 results = {"items_id": item_id}
 if q:
    results.update({"q": q})
 return results   


"""
如果你想不使用 Query 声明没有默认值的查询参数 q，同时使用 Path 声明路径参数 item_id，
并使它们的顺序与上面不同，Python 对此有一些特殊的语法。

传递 * 作为函数的第一个参数。

Python 不会对该 * 做任何事情，但是它将知道之后的所有参数都应作为关键字参数（键值对），
也被称为 kwargs，来调用。即使它们没有默认值
"""

@app.get("/items_3/{item_id}")
async def read_item3(*, item_id: int = Path(title="The id of the item to get", ge=0, le=1000), q = str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results



# 使用 Pydantic 模型的查询参数
from pydantic import BaseModel, Field
from typing import Literal

# 你可以使用 Pydantic 的模型配置来 forbid（意为禁止 —— 译者注）任何 extra（意为额外的 —— 译者注）字段
class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}
    limit: int = Field(100, gt=0,le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str]  = []

@app.get("/demo/items_123")
async def demo_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query