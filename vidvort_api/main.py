from random import choice
from string import ascii_lowercase
from fastapi import FastAPI, UploadFile
import uvicorn
from pathlib import Path

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/upload-video")
async def create_upload_video(file: UploadFile = None):
    if file is None:
        return {"filename": "No file"}

    random_str_10 = ''.join(choice(ascii_lowercase) for i in range(5))

    file_name = random_str_10 + Path(file.filename).suffix
    file_path = Path("files/uploads") / file_name
    
    with file_path.open("wb") as buffer:
        buffer.write(file.file.read())

    return {"filename": file_name}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)