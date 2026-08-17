### FastAPIのTemporary Redirectのデモコード  

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2025/09/02/231908](https://fallpoke-tech.hatenadiary.jp/entry/2025/09/02/231908)

#### 実行コマンド
以下、1,2どちらでも可能です。 

- `endpoint.py` 
1. ```python endpoint.py```
2. ```uvicorn endpoint:app --reload --port 8000```  

#### セットアップ

必要なパッケージをインストール：
```bash
pip install fastapi uvicorn python-multipart
```

#### ファイル構成

- **endpoint.py**: FastAPIアプリケーションのメインモジュール。lifespan イベント、CORS設定、HTMLレスポンス、およびメッセージ取得API を実装
- **router.py**: APIルーターモジュール。ルーター経由でのメッセージ取得API を実装
- **index.html**: フロントエンド。2つのAPI呼び出しボタンを配置し、fetch APIでバックエンドと通信

#### 機能説明

**Lifespan イベント**
- アプリケーション起動時に `"起動時に設定したメッセージ"` をアプリケーションの状態 (`Request.state`) に設定
- アプリケーション終了時にクリーンアップ処理を実行

**エンドポイント**
- `GET /`: HTMLファイル（index.html）を返すエンドポイント
- `GET /message`: 起動時に設定されたメッセージを取得するエンドポイント（メインモジュール定義）
- `GET /message2`: 起動時のメッセージに `"(router)"` を追加して返すエンドポイント（ルーター定義）

**CORS設定**
- すべてのオリジン（`allow_origins=["*"]`）からのリクエストを許可

#### 画面表示  
実行後に下記にアクセス。  
[http://localhost:8000/](http://localhost:8000/)  

#### 参考サイト  
- [https://fastapi.tiangolo.com/advanced/events/](https://fastapi.tiangolo.com/advanced/events/)
- [https://openillumi.com/fastapi-app-state-lifespan-object-reuse/](https://openillumi.com/fastapi-app-state-lifespan-object-reuse/)

---

*Author: Claude Haiku 4.5*
