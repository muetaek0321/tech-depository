### indra-ocrのお試し

### 記事

[https://fallpoke-tech.hatenadiary.jp/entry/2026/10/20/222505](https://fallpoke-tech.hatenadiary.jp/entry/2026/10/20/222505)

### 内容（LLMによる生成）

軽量かつ高速に動作するOCRモデル「indra-ocr」を用いて、画像内の日本語テキスト抽出と検出領域の可視化を行うデモ実装です。
詳しい動作や解説は上記の記事を参照してください。

#### ソースコードの説明

![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9?logo=astral&logoColor=white)
![indra-ocr](https://img.shields.io/badge/indra--ocr-FF6F00)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)

このディレクトリは、CPU環境でも高速に動作するOCRモデル「indra-ocr」を利用し、撮影画像からのテキスト抽出および検出領域（バウンディングボックス）の可視化画像を生成する検証コードで構成されています。

- `main_demo.py`
  - 事前学習済みOCRモデルのロードから推論、検出矩形の描画・画像保存までを行うメインスクリプトです。
  - `os.environ["HF_HOME"] = "./pretrained"` により、Hugging Faceからのモデルキャッシュ先をローカルの `./pretrained` に固定します。
  - `indra_ocr.load(threads=4)` でCPUマルチスレッドを指定してモデルを初期化します。
  - OpenCVで画像を読み込み、グレースケール変換したうえで `conv.ocr()` を実行してテキスト抽出と推論時間を計測します。
  - モデルが出力する回転角（`page.rotation`）に応じた正立補正を行い、`page.lines` の座標（`line.box`）に基づいて検出テキスト行を緑色の矩形枠で描画し、元の回転状態に戻して結果画像（`result_detected_*.jpg`）として保存します。

- `data/`
  - 検証用のサンプル画像（歌詞カードを撮影した写真データなど）を格納するディレクトリです。

- `pretrained/`
  - Hugging Face Hubから自動ダウンロードされた `indra-ocr` の事前学習済みモデルファイルを保持するローカルキャッシュディレクトリです。

- `pyproject.toml`
  - uvで管理するプロジェクト設定ファイルです。Python 3.13以上を対象とし、`indra-ocr` の依存関係や Ruff によるコードフォーマット・リントの設定を定義しています。

Author: *Gemini 3.8 Flash*
