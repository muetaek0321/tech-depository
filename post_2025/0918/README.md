### 画像分類モデルDeiTのデモコード

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2025/09/18/233529](https://fallpoke-tech.hatenadiary.jp/entry/2025/09/18/233529)

### 元コード
[https://huggingface.co/facebook/deit-base-distilled-patch16-224](https://huggingface.co/facebook/deit-base-distilled-patch16-224)

#### ソースコードの説明
`deit_demo.py` は、Hugging Face Transformers の `facebook/deit-base-distilled-patch16-224` 画像分類モデルを使ったデモです。実行時にまず `./pretrained` ディレクトリを作成し、`HF_HOME` をこのローカルディレクトリに設定してモデルと関連キャッシュを保存します。次に、`requests` で COCO データセットのサンプル画像を取得し、`PIL.Image` で読み込みます。

`AutoFeatureExtractor` により入力画像をモデルが扱えるテンソル形式に変換し、`DeiTForImageClassificationWithTeacher` を使って推論を行います。出力の `logits` の最大値を取ることで予測クラスを識別し、モデルの `config.id2label` からクラス名を出力します。

Author: *Raptor mini*
