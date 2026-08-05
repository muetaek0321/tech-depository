import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from PIL import Image

from modules.convert_image_base64 import image_to_bytes
from modules.prompt import PROMPT

# 環境変数の読み込み
load_dotenv()


def main():
    # 画像の読み込み
    img = Image.open("sample.jpg")
    # 画像をBase64文字列に変換
    image_base64 = image_to_bytes(img)

    # モデルの設定
    llm = ChatOllama(
        model="minimax-m3:cloud",
        base_url="https://ollama.com",
        api_key=os.getenv("OLLAMA_API_KEY", None),
        temperature=0.0,
    )

    # プロンプトの設定
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": PROMPT,
            },
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{image_base64}"},
            },
        ]
    )

    # 返答の生成
    response = llm.invoke([message])

    # 生成された返答の取得
    print(response.content)


if __name__ == "__main__":
    main()
