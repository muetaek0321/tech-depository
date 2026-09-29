### FastAPIのTemporary Redirectのデモコード  

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2025/07/17/232923](https://fallpoke-tech.hatenadiary.jp/entry/2025/07/17/232923)

#### 実行コマンド
以下、1,2どちらでも可能です。 

- `endpoint_1.py` 
1. ```python endpoint_1.py```
2. ```uvicorn endpoint_1:app --reload --port 8000```

- `endpoint_2.py` 
1. ```python endpoint_2.py```
2. ```uvicorn endpoint_2:app --reload --port 8080```

テストする場合は`endpoint_1.py`と`endpoint_2.py`を両方立ち上げてください。  

#### 画面表示  
実行後に下記にアクセス。  
[http://localhost:8000/](http://localhost:8000/)  

#### 参考サイト  
- [https://fastapi.tiangolo.com/ja/advanced/custom-response/#redirectresponse](https://fastapi.tiangolo.com/ja/advanced/custom-response/#redirectresponse)
- [https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Status/307](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Status/307)  
- [https://qiita.com/naka_kyon/items/6afe6c1ead871977a15a](https://qiita.com/naka_kyon/items/6afe6c1ead871977a15a)  

#### ソースコードの説明

このディレクトリは、FastAPI の `RedirectResponse`（HTTP 307 Temporary Redirect）を用いて、あるエンドポイントから別のエンドポイントへリクエストを転送するデモアプリケーションです。2つのFastAPIサーバー間でリダイレクトを行い、画像ダウンロードやテキスト取得がリダイレクト経由でも動作することを確認できます。

- `endpoint_1.py`
  - ポート8000で動作するメインのFastAPIサーバー
  - `GET /` : `index.html` を読み込み `HTMLResponse` で返すフロントエンド表示用エンドポイント
  - `GET /img_1` : `data/dog.png` を `FileResponse` で直接返す画像ダウンロードエンドポイント
  - `GET /img_2` : `RedirectResponse`（ステータスコード307）で `endpoint_2` の `/img` へリダイレクトする
  - `GET /message_1` : 自身のサーバーからテキストメッセージを直接返すエンドポイント
  - `GET /message_2` : `RedirectResponse`（ステータスコード307）で `endpoint_2` の `/message` へリダイレクトする
  - CORSミドルウェアを設定し、全オリジンからのアクセスを許可
  - 依存ライブラリ: `fastapi`, `uvicorn`

- `endpoint_2.py`
  - ポート8080で動作するリダイレクト先のFastAPIサーバー
  - `GET /img` : `data/cat.png` を `FileResponse` で返す画像ダウンロードエンドポイント
  - `GET /message` : テキストメッセージを返すエンドポイント
  - 依存ライブラリ: `fastapi`, `uvicorn`

- `index.html`
  - `endpoint_1` がルート (`/`) で配信するデモ用HTMLページ
  - 4つのボタンを配置し、それぞれ直接取得とリダイレクト経由の取得を比較できる構成
    - 画像ダウンロード（直接 `/img_1`）とリダイレクト経由（`/img_2` → `endpoint_2` の `/img`）
    - テキスト取得（直接 `/message_1`）とリダイレクト経由（`/message_2` → `endpoint_2` の `/message`）
  - JavaScript の `fetch` 関数でテキスト取得APIを呼び出し、結果を `alert` で表示

- `data/`
  - `dog.png` : `endpoint_1` の `/img_1` で返される画像ファイル
  - `cat.png` : `endpoint_2` の `/img` で返される画像ファイル

Author: *Claude Opus 4.6*
