import os
import hashlib
import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI()

SERVER_PATH = "target"
TOKEN = "12345678"


def hash_file(file_path):
    try:

        hasher = hashlib.md5()
        with open(file_path, 'rb') as file:
            buf = file.read()
            hasher.update(buf)
        return hasher.hexdigest()

    except FileNotFoundError:
        return "-1"


@app.post("/get_file_hash")
def get_file_hash(file_name: str):
    file_path = os.path.join(SERVER_PATH, file_name)
    file_hash = hash_file(file_path)
    return {"file_hash": file_hash}


@app.post("/upload_file")
async def upload_file(file_name: str, file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="File not provided")

    file_path = os.path.join(SERVER_PATH, file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as new_file:
        new_file.write(await file.read())

    return {"detail": "File uploaded successfully"}


uvicorn.run(app, host="0.0.0.0", port=8000)
