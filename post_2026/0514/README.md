### FastAPI Dependsのデモ

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2026/05/14/212757](https://fallpoke-tech.hatenadiary.jp/entry/2026/05/14/212757)

### 内容（GitHub Copilotによる生成）

#### ソースコードの説明

##### models.py
Pydantic の BaseModel を継承した `CamelModel` クラスを定義しています。
- `alias_generator=to_camel` により、Python の snake_case フィールド名を JSON の camelCase 形式に自動変換
- `populate_by_name=True` により、元の snake_case 名でも受け取り可能
- リクエスト/レスポンス時のデータ形式変換を統一的に管理するための基底クラス

##### main.py
FastAPI アプリケーションのメインロジックです。

**モデルの定義：**
- `RequestModel`: クエリパラメータを受け取るためのモデル（user_id, user_name を持つ）
- `ResponseModel`: API レスポンスとして返すモデル（user_id, user_name, message を持つ）
- 両者とも CamelModel を継承し、snake_case ↔ camelCase 変換機能を備えている

**依存性関数：**
- `get_endpoint_logger(req: Request)`: Depends() で使用される依存性関数
  - リクエストオブジェクトからエンドポイント名を取得
  - ロギングを設定して、該当エンドポイント用のロガーを返す
  - 複数のエンドポイントで共通のロギング処理を再利用可能

**エンドポイント：**
- `GET /`: ルートエンドポイント、Swagger UI ドキュメントにリダイレクト
- `GET /test`: Depends() を使ったメイン動作例
  - `query: Annotated[RequestModel, Depends()]` で query パラメータを RequestModel に自動マッピング
  - `logger: Annotated[logging.Logger, Depends(get_endpoint_logger)]` で依存性関数を呼び出してロガーを注入
  - RequestModel のデータを変換なし/変換ありで表示
  - ResponseModel を返す

**FastAPI Depends の活用：**
- 複雑な依存関係を宣言的に管理できる
- 同じ依存性ロジックを複数のエンドポイント間で共有
- テストやモック化が容易
- ロギング、認証、バリデーションなどのクロスカッティングコンサーン適用に最適



