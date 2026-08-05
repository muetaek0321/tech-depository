### LangChainのChatで画像入力をお試し

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2026/08/06/003507](https://fallpoke-tech.hatenadiary.jp/entry/2026/08/06/003507)

### 内容（GitHub Copilotによる生成）

#### ソースコードの説明

このディレクトリは、LangChain の Chat 機能で画像入力付きの対話を試すサンプルです。

- `main_googlegenai.py`
  - `langchain_google_genai.ChatGoogleGenerativeAI` を使い、Google の Gemma モデルへ画像付きメッセージを送信します。
  - `sample.jpg` を `PIL.Image` で開き、`modules.convert_image_base64.image_to_bytes` で Base64 エンコードします。
  - `modules.prompt.PROMPT` のテキストと `image_url` のデータ URI を `HumanMessage` にまとめてモデルに渡します。
  - 返却された `response.content` のテキスト応答を出力します。

- `main_ollama_cloud.py`
  - `langchain_ollama.ChatOllama` を使い、クラウド版 Ollama の `minimax-m3:cloud` モデルへ同じ画像付きプロンプトを送信します。
  - `OLLAMA_API_KEY` を `.env` から読み込み、`base_url` に `https://ollama.com` を指定します。
  - こちらも `HumanMessage` の `content` にテキストと `image_url` を含め、返答を表示します。

- `main_ollama_local.py`
  - ローカル実行可能な Ollama モデル `qwen3.5:9b` を使用するバージョンです。
  - クラウド版と同様に画像を Base64 に変換し、`HumanMessage` へ渡して応答を取得します。

- `modules/convert_image_base64.py`
  - `PIL.Image` を受け取り、PNG 形式で `BytesIO` に保存して Base64 エンコードした文字列を返すユーティリティです。
  - 画像が RGB 以外のモードの場合は `convert("RGB")` で変換します。

- `modules/prompt.py`
  - モデルへ渡す日本語プロンプトを定義しています。
  - 画像の観察結果を分かりやすく説明させるための指示が含まれています。

- `pyproject.toml`
  - `langchain-google-genai`, `langchain-ollama`, `pillow`, `python-dotenv` などの依存関係を管理します。
  - Python 3.13 以上を前提としています。

このサンプルは、画像を Base64 データ URI として LLM に渡し、視覚情報を含むチャット応答を得る流れを確認することが目的です。

Author: *Raptor mini*

