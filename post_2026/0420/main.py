from pprint import pprint
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from models import CamelModel


app = FastAPI()


class RequestModel(CamelModel):
    """リクエスト用のBaseModel"""
    user_id: int = 1234
    user_name: str = "test_user"
    

class ResponseModel(CamelModel):
    """レスポンス用のBaseModel"""
    user_id: int
    user_name: str
    message: str


@app.get("/")
def root() -> dict:
    """ルートエンドポイント"""
    return RedirectResponse(url="/docs")


@app.post("/test")
def base_model_test_1(
    pyload: RequestModel
) -> ResponseModel:
    """postメソッドでテスト"""
    # 受け取ったリクエストモデルを表示
    pprint(pyload.model_dump())
    
    # レスポンスモデルを返す
    response = ResponseModel(
        user_id=pyload.user_id,
        user_name=pyload.user_name,
        message="postメソッドでレスポンスモデルのテスト"
    )
    
    return response
    

@app.get("/test")
def base_model_test_2(
    query: Annotated[RequestModel, Depends()]
) -> ResponseModel:
    """getメソッドでテスト"""
    # 受け取ったリクエストモデルを表示
    pprint(query.model_dump())
    
    # レスポンスモデルを返す
    response = ResponseModel(
        user_id=query.user_id,
        user_name=query.user_name,
        message="getメソッドでレスポンスモデルのテスト"
    )
    
    return response


if __name__ == "__main__":
    uvicorn.run(app)

