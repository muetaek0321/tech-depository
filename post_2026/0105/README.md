### 日本語を含むファイル名のファイルをダウンロードするAPIのサンプル  

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2026/01/05/001123](https://fallpoke-tech.hatenadiary.jp/entry/2026/01/05/001123)

#### 実行コマンド
以下、1,2どちらでも可能です。  
1. ```python main.py```
2. ```uvicorn main:app --reload```

#### 画面表示
実行後に下記にアクセス。  
[http://localhost:8000/](http://localhost:8000/)


### 内容（GitHub Copilotによる生成）

#### main.py
FastAPIを使用した日本語ファイルダウンロード機能のデモンストレーションプログラムです。

- **目的**: 日本語を含むファイル名でのCSVファイルダウンロード機能の実装例を示す
- **処理内容**:
  - ローカルにファイルを保存せず、メモリ内でDataFrameをCSV形式に変換
  - StreamingResponseを使用してクライアントにストリーミング配信
  - `/download` エンドポイント: UTF-8エンコーディング（RFC 2231形式）でヘッダーを正しく設定し、日本語ファイル名が正しくダウンロードされる方式
  - `/download_error` エンドポイント: UTF-8エンコーディングなしの設定で、日本語ファイル名ダウンロードがエラーになる方式を比較
  - サンプルデータ: バンドメンバー（Miyamoto、Ishimori、Takamidori、Tominaga）の情報（ボーカル/ギター、ギター、ベース、ドラム）をDataFrameで管理

#### index.html
FastAPIサーバーに接続するUIを提供するHTMLファイルです。

- **目的**: ブラウザからダウンロード機能にアクセスするためのインターフェース提供
- **処理内容**:
  - `/download` エンドポイントにアクセスするダウンロードボタン（正常形式）
  - `/download_error` エンドポイントにアクセスするダウンロードボタン（エラー形式）
  - 2つのダウンロード方式の動作差を比較できる構成

#### sample.csv
サンプルデータとしてのCSVファイルです。

- **内容**: main.py内で定義されるサンプルデータをCSV形式で保存したファイル
- **用途**: ダウンロード機能のテスト時に参照


