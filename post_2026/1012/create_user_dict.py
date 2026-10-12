"""
参考：
https://zenn.dev/hosyan/articles/c54abbb5cac5dd
"""

import json
import os
import re

from dotenv import load_dotenv
from google import genai

load_dotenv()


PROMPT = """
あなたは日本語の楽曲タイトルの読み仮名推定を行うアシスタントです。
次の楽曲タイトルの読みを、全角カタカナで1つだけ返してください。

ルール:
- 返答は全角カタカナのみとする
- 日本語・カタカナ・英字・記号が混ざっていても、最も自然な読みを推定する
- 促音・長音・語尾の変化は自然な日本語として扱う
- 返答は JSON 形式のみとし、キーは "reading" にする
- 読みが曖昧な場合でも、最も自然な仮名表記を返す
- 余計な説明やコードブロックは付けない
- ひらがなや英字は使わず、必ず全角カタカナに変換する

例:
- "星の砂" -> {{"reading":"ホシノスナ"}}
- "さよならパーティー" -> {{"reading":"サヨナラパーティー"}}
- "DEAD OR ALIVE" -> {{"reading":"デッドオアアライブ"}}
- "ハロー New York!" -> {{"reading":"ハローニューヨーク"}}

タイトル: {keyword}
"""


def main() -> None:
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    keywords = []

    # 例として曲名のリストを与える
    examples = [
        "今宵の月のように",
        "風",
        "悪魔メフィスト",
        "漂う人の性",
        "FLYER",
        "Hello. I love you",
        "ヒトコイシクテ、アイヲモトメテ",
    ]

    for title in examples:
        # LLMでキーワードの読みを取得する
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite", contents=PROMPT.format(keyword=title)
        )

        reading = title
        try:
            result = json.loads(response.text.strip())
            if isinstance(result, dict) and "reading" in result and result["reading"]:
                reading = result["reading"]
        except Exception:
            text = response.text.strip()
            match = re.search(r'"reading"\s*:\s*"([^"]+)"', text)
            if match:
                reading = match.group(1)
            elif text:
                reading = text.strip().strip("\"'`")

        print(f"{title} -> {reading}")
        keyword_info = []
        keyword_info.append(title)  # - 0 見出し (TRIE 用)
        keyword_info.append("4786")  # - 1 左連接ID
        keyword_info.append("4786")  # - 2 右連接ID
        keyword_info.append("1")  # - 3 コスト
        keyword_info.append(title)  # - 4 見出し (解析結果表示用)
        keyword_info.append("名詞")  # - 5 品詞1
        keyword_info.append("固有名詞")  # - 6 品詞2
        keyword_info.append("曲名")  # - 7 品詞3
        keyword_info.append("*")  # - 8 品詞4
        keyword_info.append("*")  # - 9 品詞 (活用型)
        keyword_info.append("*")  # - 10 品詞 (活用形)
        keyword_info.append(reading)  # - 11 読み
        keyword_info.append(title)  # - 12 正規化表記
        keyword_info.append("*")  # - 13 辞書形ID
        keyword_info.append("*")  # - 14 分割タイプ
        keyword_info.append("*")  # - 15 A単位分割情報
        keyword_info.append("*")  # - 16 B単位分割情報
        keyword_info.append("*")  # - 17 ※未使用

        keywords.append(keyword_info)

    with open("./keywords.csv", mode="w", encoding="utf-8") as f:
        for keyword in keywords:
            f.write(",".join(keyword) + "\n")


if __name__ == "__main__":
    main()
