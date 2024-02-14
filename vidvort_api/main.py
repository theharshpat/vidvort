from fastapi import FastAPI, UploadFile
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/upload-video")
async def create_upload_video():
    return {"filename": "video.mp4"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)