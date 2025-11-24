from fastapi import FastAPI, Form, UploadFile, File
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}



class FormModel(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"} # 来禁止（ forbid ）任何额外（ extra ）字段


@app.post("/login/")
async def login(data: Annotated[FormModel, Form()]):
    return data.username


@app.post("/files/")
async def create_file(file: bytes | None = File(default=None)): # 可选上传

    """
    如果把路径操作函数参数的类型声明为 bytes，FastAPI 将以 bytes 形式读取和接收文件内容。

    这种方式把文件的所有内容都存储在内存里，适用于小型文件
    """
    return {"file": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile()):
    """
    UploadFile 与 bytes 相比有更多优势：

    使用 spooled 文件：
    存储在内存的文件超出最大上限时，FastAPI 会把文件存入磁盘；
    这种方式更适于处理图像、视频、二进制文件等大型文件，好处是不会占用所有内存；
    可获取上传文件的元数据；
    自带 file-like async 接口；
    暴露的 Python SpooledTemporaryFile 对象，可直接传递给其他预期「file-like」对象的库
    """
    return {"filename": file.filename}



# FastAPI 支持同时使用 File 和 Form 定义文件和表单字段。

@app.post("/files/")
async def create_file(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }