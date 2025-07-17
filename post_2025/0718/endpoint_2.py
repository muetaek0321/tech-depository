from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn


app = FastAPI()


@app.get("/img")
def show_img() -> FileResponse:
    """ファイルをダウンロードするAPI
    """
    filepath = Path("./data/cat.png")
    
    return FileResponse(filepath, media_type="image/png", filename=filepath.name)


@app.get("/message")
def get_message() -> str:
    """ファイルをダウンロードするAPI
    """
    return "endpoint_2.pyからのメッセージです。"


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
