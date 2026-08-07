### YomiTokuを自作プログラムに組み込むデモ

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2025/10/22/000348](https://fallpoke-tech.hatenadiary.jp/entry/2025/10/22/000348)

#### ソースコードの説明
`use_yomitoku_test.py` は `yomitoku` の `TextDetector` と `TextRecognizer` を使って、`./images` 配下の画像から文字領域を検出し、検出した領域を切り出してテキスト認識を行います。

- `os.environ["HF_HOME"] = "./pretrained"` でモデルキャッシュ先をローカルの `pretrained` フォルダに設定します。
- `TextDetector()` で画像内の文字領域を検出し、検出した領域を順にクロップします。
- クロップした画像は `./result` フォルダに保存し、`TextRecognizer()` でテキストを抽出します。
- 抽出したテキストは `・` に変換してから `annotations.csv` に保存します。
- 最終的に `./result/annotations.csv` に `img` と `text` の対応を出力します。

#### Author
*Raptor mini*


