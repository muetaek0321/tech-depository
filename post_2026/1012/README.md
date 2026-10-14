### uv環境でSudachiPyのユーザ辞書を設定

### 記事

[https://fallpoke-tech.hatenadiary.jp/entry/2026/10/12/223235](https://fallpoke-tech.hatenadiary.jp/entry/2026/10/12/223235)

### 内容（LLMによる生成）

uv環境でSudachiPyのユーザ辞書（曲名情報など）を作成・設定し、形態素解析で固有名詞として抽出するサンプルです。
詳しい動作や解説は上記の記事を参照してください。

#### ソースコードの説明

![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9?logo=astral&logoColor=white)
![SudachiPy](https://img.shields.io/badge/SudachiPy-2596be)
![Gemini API](https://img.shields.io/badge/Gemini%20API-8E75C2?logo=google&logoColor=white)

このディレクトリは、Gemini APIで楽曲タイトルの読み仮名を推定してSudachiPy用のユーザ辞書を作成し、形態素解析で曲名を固有名詞として抽出するコードと設定ファイルで構成されています。

- `create_user_dict.py`
  - Gemini API（`gemini-3.5-flash-lite`）を使い、楽曲タイトルから全角カタカナの読み仮名をJSON形式で取得します。
  - 見出し、連接ID、コスト、品詞情報（名詞,固有名詞,曲名,*,*,*）、読み、正規化表記など、Sudachiの仕様に合わせたCSVレコードを組み立てます。
  - 整形したデータを `keywords.csv` としてUTF-8で保存します。
  - `python-dotenv` で `.env` から API キーを読み込みます。

- `main_test.py`
  - SudachiPyを使ってテキストを形態素解析し、登録した曲名を抽出して確認するスクリプトです。
  - `MorphologicalExtraction` クラスで形態素解析器を初期化し、`extract_songs()` で文を形態素に分割します。
  - 分割モードには複合語を1単語として扱う `SplitMode.C` を指定し、品詞情報の3番目が「曲名」の形態素を抽出して正規化表記のリストを返します。
  - サンプル文章「今宵の月のようにと風という曲が好きです。」を解析し、各形態素の表層形・品詞・正規化表記を表示します。

- `sudachi.json`
  - SudachiPyの設定ファイルです。
  - `userDict` に `user.dic` を指定し、作成したユーザ辞書を読み込みます。
  - 長音記号の統一（`ProlongedSoundMarkPlugin`）や括弧内読み仮名の無視（`IgnoreYomiganaPlugin`）、未知語処理など、形態素解析に必要なプラグインを設定しています。

- `keywords.csv`
  - `create_user_dict.py` が出力したユーザ辞書の元データ（CSV形式）です。品詞「名詞,固有名詞,曲名」として各楽曲のエントリが記録されています。

- `user.dic`
  - `keywords.csv` をもとに、`sudachipy ubuild` コマンドなどでコンパイルされたバイナリ形式のユーザ辞書です。

- `pyproject.toml`
  - uvで管理するプロジェクトの設定ファイルです。Python 3.13以上を対象とし、`sudachipy`、`sudachidict-core`、`google-genai`、`python-dotenv` などの依存関係と Ruff の設定を定義しています。

Author: *Gemini 3.8 Flash*

