from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found", headers={
            "X-Error": "These goes my error"
        })
    return  items[item_id]    


class UnicornException(Exception):
    def __init__(self, **args: dict) -> None:
        super().__init__(*args)
        self.name = args["name"]


@app.exception_handler(UnicornException)
async def unicorn_exception_hander(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."}
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name != 'J':
       raise UnicornException(name=name)
    return {"unicorn_name": name}


# 覆盖默认的异常
from starlette.exceptions import HTTPException as StarletteException
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError


@app.exception_handler(StarletteException)
async def http_exception_handler(request: Request, exc: StarletteException):
    return PlainTextResponse(status_code=exc.status_code, content=str(exc.detail))


@app.exception_handler(RequestValidationError)
async def request_validation_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(status_code=400, content=str(exc))


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    print(item_id,'--')
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}