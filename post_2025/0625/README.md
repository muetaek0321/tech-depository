### FastAPIのapp.stateのデモコード  

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2025/06/25/000521](https://fallpoke-tech.hatenadiary.jp/entry/2025/06/25/000521)

#### 実行コマンド
以下、1,2どちらでも可能です。  
1. ```python main.py```
2. ```uvicorn main:app --reload```

#### 画面表示
実行後に下記にアクセス。  
[http://localhost:8000/](http://localhost:8000/)

#### ソースコードの説明

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=white)

このディレクトリは、FastAPIの `app.state` を使ってアプリケーション全体で状態（メッセージ）を共有する方法を示すデモコードです。メインモジュールで保存した値を、同一ファイル内のエンドポイントおよび別ファイルの `APIRouter` 経由のエンドポイントの両方から取得できることを確認できます。

- `main.py`
  - FastAPIアプリケーションのエントリポイント
  - `GET /` で `index.html` を返す画面表示用エンドポイントを定義
  - `POST /text` で受け取ったテキストを `app.state.message` に格納
  - `GET /message` で `app.state.message` から値を取り出して返却
  - `router/sub.py` のルーターを `include_router` で組み込み
  - `modules` ディレクトリを `StaticFiles` としてマウントし、JSファイルを配信
  - CORSミドルウェアを設定（全オリジン許可）

- `router/sub.py`
  - `APIRouter` を使った別ファイルのエンドポイント定義
  - `GET /sub/message` で `request.app.state` 経由でメッセージを取得
  - メインモジュールと異なるファイルからでも `app.state` にアクセスできることを示す

- `modules/types.py`
  - `POST /text` のリクエストボディ用Pydanticモデル `Text` を定義

- `modules/postText.js`
  - フォームの送信イベントを受け取り、入力テキストを `POST /text` へJSON形式で送信するフロントエンド処理

- `modules/getMessage.js`
  - 指定パスのAPIからデータを取得し、アラートで表示する `fetchData` 関数を定義

- `index.html`
  - テキスト入力フォームと、メッセージ取得ボタン（メイン / router経由）を配置したデモ画面

Author: *Claude Opus 4.6*
