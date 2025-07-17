from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_url = "http://localhost:8080"

@app.get("/")
def main_page() -> HTMLResponse:
    """htmlファイルを読み込んで表示するAPI
    """
    with open("./index.html", mode='r', encoding='utf-8') as f:
        content = f.read()
        
    return HTMLResponse(content=content)


@app.get("/img_1")
def show_img_1() -> FileResponse:
    """ファイルをダウンロードするAPI
    """
    filepath = Path("./data/dog.png")
    
    return FileResponse(filepath, media_type="image/png", filename=filepath.name)


@app.get("/img_2")
def show_img_2() -> RedirectResponse:
    """ファイルをダウンロードするAPI
    """
    return RedirectResponse(api_url+"/img", status_code=307)


@app.get("/message_1")
def get_message_1() -> str:
    """ファイルをダウンロードするAPI
    """
    return "endpoint_1.pyからのメッセージです。"


@app.get("/message_2")
def get_message_2() -> RedirectResponse:
    """ファイルをダウンロードするAPI
    """
    return RedirectResponse(api_url+"/message", status_code=307)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
