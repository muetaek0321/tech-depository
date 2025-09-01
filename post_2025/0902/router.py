from fastapi import APIRouter, Request


router = APIRouter()


@router.get("/message2")
async def get_message_2(
    req: Request
) -> str:
    """メッセージ取得API
    """
    print("メッセージ取得（router）")
    
    # 起動時に設定したメッセージを取得
    msg = req.state.msg

    return msg + "(router)"