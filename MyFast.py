# pip install fastapi 
# pip install uvicorn
# uvicorn MyFast:app --reload   
from typing import Union

from fastapi import FastAPI , File, UploadFile, Header, Response
from fastapi.responses import HTMLResponse

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/test")
def read_test():
    return {"test": "testWorld"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name , "item_price": item.price}


@app.post("/files/")
async def create_files(files: list[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/upForm")
async def main():
    content = """
<body>
<form action="/photos/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = f"files/{filename}"
    return File(file_path, filename=filename)

@app.get("/photos/{filename}")
async def download_image(filename: str):
    file_path = f"./photos/{filename}"
    # return File(file_path, filename=filename, media_type="image/jpeg")
    return Response(File(file_path, filename=filename, media_type="image/jpeg"))

@app.post("/photos")
async def upload_image(file: UploadFile):
    file_path = f"./photos/{file.filename}"
    print(file_path)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename}

