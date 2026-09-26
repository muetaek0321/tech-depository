### RF-DETRのデモコード

### 記事

[https://fallpoke-tech.hatenadiary.jp/entry/2026/09/26/222559](https://fallpoke-tech.hatenadiary.jp/entry/2026/09/26/222559)

### 内容（LLMによる生成）

物体検出モデル「RF-DETR」を用いて、画像内の物体検出および結果のバウンディングボックス描画を行うデモ実装です。
詳しい動作や解説は上記の記事を参照してください。

#### ソースコードの説明

このディレクトリは、Hugging Face Transformersの「RF-DETR」モデルを用いて入力画像に対する物体検出を実行し、推論結果をバウンディングボックスで可視化するデモコードで構成されています。

- `demo.py`
  - **目的**: 事前学習済みRF-DETRモデルをロードして物体検出を実行し、推論時間の計測・結果出力および可視化を行うメインスクリプトです。
  - **主要な処理内容**:
    - `os.environ["HF_HOME"] = "./pretrained"` により、事前学習済みモデルのキャッシュ先をローカルディレクトリに指定。
    - `transformers` の `AutoImageProcessor` と `RfDetrForObjectDetection` を使用し、事前学習済みモデル（`stevenbucaille/rf-detr-base`）をロード。
    - 入力画像（`2008_002610.jpg`）を読み込んでテンソル化し、`torch.no_grad()` で推論を実行。`time.perf_counter` により推論時間を計測。
    - `processor.post_process_object_detection` でスコア閾値 0.5 以上の検出結果（バウンディングボックス、ラベル、スコア）を後処理・コンソール表示（上位8件）。
    - `visualize.py` の `show_detections` を呼び出し、結果を画像上に描画して表示。

- `visualize.py`
  - **目的**: 物体検出の推論結果（矩形座標・ラベル名・信頼度スコア）を画像上に描画・表示するための可視化ユーティリティモジュールです。
  - **主要な関数**:
    - `_generate_colors(n: int)`: 検出クラス数に応じてHSV色空間から重複しにくいRGBカラーを動的に生成。
    - `draw_detections(image, results, id2label, line_width=3, font_size=16)`: PIL（`ImageDraw`, `ImageFont`）を利用して各バウンディングボックスとラベル背景・テキストを描画（画像上端ではみ出す場合のラベル配置反転処理を含む）。
    - `show_detections(image, results, id2label, figsize=(12, 8))`: 描画済み画像を `matplotlib.pyplot` を使用してウィンドウ表示。

- `2008_002610.jpg`
  - 物体検出の動作確認用サンプル画像。

- `pretrained/`
  - Hugging Faceからダウンロードされたモデルファイル等を保持するローカルキャッシュディレクトリ。

Author: *Gemini 3.8 Flash*
