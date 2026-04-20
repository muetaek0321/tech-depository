### pydantic BaseModelのAliasGeneratorのデモ

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2026/04/20/211113](https://fallpoke-tech.hatenadiary.jp/entry/2026/04/20/211113)

### 内容（GitHub Copilotによる生成）

#### ソースコードの説明

##### models.py
Pydantic v2のAliasGeneratorを使用して、snake_case（例：`user_name`）とcamelCase（例：`userName`）の相互変換を行うベースモデルを定義しています。

- `CamelModel`：継承用の基盤クラス
  - `alias_generator=to_camel`：プロパティをcamelCaseに変換
  - `populate_by_name=True`：元の名前でも代入を受け付ける

##### main.py
FastAPIアプリケーションで、AliasGeneratorの動作をテストしています。

- `RequestModel`：リクエスト用モデル（`user_id`, `user_name`）
- `ResponseModel`：レスポンス用モデル（`user_id`, `user_name`, `message`）
- `POST /test`：POSTメソッドでリクエストを受け取り、内部表現と外部表現（camelCase）の変換結果を表示
- `GET /test`：GETメソッドでクエリパラメータを受け取り、同様に変換結果を表示

`model_dump()`と`model_dump(by_alias=True)`の違いを確認できます。

#### 実行方法

##### 1. 依存パッケージのインストール
```bash
pip install fastapi uvicorn pydantic
```

##### 2. アプリケーションの起動
```bash
python main.py
```

##### 3. テスト方法

**ブラウザでのテスト：**
- `http://localhost:8000/docs` にアクセスするとSwagger UIが表示されます
- APIのテストはここから実施できます

**POSTメソッドのテスト例：**
```bash
curl -X POST "http://localhost:8000/test" \
  -H "Content-Type: application/json" \
  -d '{"userId": 5678, "userName": "john_doe"}'
```

**GETメソッドのテスト例：**
```bash
curl "http://localhost:8000/test?userId=5678&userName=john_doe"
```

**実行時の出力例：**
```
変換なし: {'user_id': 5678, 'user_name': 'john_doe'}
変換あり: {'userId': 5678, 'userName': 'john_doe'}
```

