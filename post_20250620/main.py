from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from modules.types import *


app = FastAPI()

# /modules というURLで modules フォルダ内のファイルを配信
app.mount("/modules", StaticFiles(directory="modules"), name="modules")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)


@app.get("/")
def main_page() -> HTMLResponse:
    """htmlファイルを読み込んで表示するAPI
    """
    with open("./index.html", mode='r', encoding='utf-8') as f:
        content = f.read()
        
    return HTMLResponse(content=content)


@app.post("/text")
def record_message(
    obj: Text
) -> str:
    """入力したテキストを記録
    """
    text = obj.text
    print(text)
    
    # stateに格納
    app.state.message = text
    
    return "OK"


@app.get("/message")
def download_from_df() -> str:
    """記録したメッセージを取り出す
    """
    # stateから取り出し
    message = app.state.message
    
    return message


if __name__ == "__main__":
    uvicorn.run(app)
