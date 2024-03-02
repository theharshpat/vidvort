from random import choice
from string import ascii_lowercase
from fastapi import FastAPI, UploadFile
import uvicorn
from pathlib import Path
import subprocess

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/videos")
async def create_video(file: UploadFile = None):
    if file is None:
        return {"filename": "No file"}
    
    if file.content_type not in ["video/mp4", "video/avi", "video/mov", "video/mkv", "video/flv", "video/quicktime", "video/webm", "video/3gpp"]:
        return {"error": "Invalid file type"}

    random_str_10 = ''.join(choice(ascii_lowercase) for i in range(5))

    file_name = random_str_10 + Path(file.filename).suffix
    file_path = Path("files/uploads") / file_name
    
    with file_path.open("wb") as buffer:
        buffer.write(file.file.read())

    return {"video_id": file_name}

@app.post("/videos/{video_id}/transcode")
async def transcode_video(video_id: str):
    target_path = Path("files/transcoded") / video_id
    subprocess.run(f"rm -f {target_path}", shell=True)
    command = f"ffmpeg -i files/uploads/{video_id} -c:v h264_videotoolbox -c:a aac -preset medium -vf 'scale=-2:480' -b:v 1000k -b:a 128k files/transcoded/{video_id}"
    subprocess.run(command, shell=True)
    return { "status": "success" }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)