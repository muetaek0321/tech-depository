from fastapi import APIRouter, Request


router = APIRouter(prefix="/sub")


@router.get("/message")
def get_message(
    req: Request
) -> str:
    """記録したメッセージを取り出す
    """
    # stateから取り出し
    message = req.app.state.message
    
    return message
