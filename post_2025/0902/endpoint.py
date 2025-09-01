from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # アプリ起動時の処理
    print("アプリ起動")
    
    yield {"msg": "起動時に設定したメッセージ"}
    
    # アプリ終了時の処理
    print("アプリ終了")


app = FastAPI(lifespan=lifespan)

app.include_router(router)

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


@app.get("/message")
def get_message_1(
    req: Request
) -> str:
    """メッセージ取得API
    """
    print("メッセージ取得")
    
    # 起動時に設定したメッセージを取得
    msg = req.state.msg
    
    return msg


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
