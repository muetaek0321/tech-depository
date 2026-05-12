import logging
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends, Request
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
    
    
def get_endpoint_logger(req: Request) -> logging.Logger:
    """APIエンドポイント用のロガーを取得する関数

    Args:
        req (Request): APIエンドポイントのRequestオブジェクト

    Returns:
        logging.Logger: APIエンドポイント用のロガーのインスタンス
    """
    endpoint_name = req.url.path
    
    # ロギングの基本設定
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )
    
    return logging.getLogger(endpoint_name)


@app.get("/")
def root() -> dict:
    """ルートエンドポイント"""
    return RedirectResponse(url="/docs")
    

@app.get("/test")
def base_model_test(
    query: Annotated[RequestModel, Depends()],
    logger: Annotated[logging.Logger, Depends(get_endpoint_logger)]
) -> ResponseModel:
    """getメソッドでテスト"""
    # 受け取ったリクエストモデルを表示
    logger.info(f"変換なし: {query.model_dump()}")
    logger.info(f"変換あり: {query.model_dump(by_alias=True)}")
    
    # レスポンスモデルを返す
    response = ResponseModel(
        user_id=query.user_id,
        user_name=query.user_name,
        message="getメソッドでレスポンスモデルのテスト"
    )
    
    return response


if __name__ == "__main__":
    uvicorn.run(app)

