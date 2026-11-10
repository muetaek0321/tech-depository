### Python標準モジュール「mmap」のデモ（改良版）

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2025/05/01/000551](https://fallpoke-tech.hatenadiary.jp/entry/2025/05/01/000551)

#### 改良前のコード
[https://github.com/muetaek0321/tech-depository/tree/main/post_2025/0430](https://github.com/muetaek0321/tech-depository/tree/main/post_2025/0430)

#### ソースコードの説明

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)

このディレクトリは、Python標準モジュール `mmap` を用いたプロセス間通信（共有メモリ）により、画像データおよびそのメタ情報（幅・高さ）を受け渡すデモコードです。区切り文字（`<SEP>`）と終端文字（`<END>`）を導入することで、固定長のオフセット指定に依存せず、画像サイズの変化に柔軟に対応できる実装となっています。

- `process1.py`
  - 送信側プロセスの実装
  - `img.png` を読み込んで指定サイズにリサイズし、画像配列をバイト列化（`img.tobytes()`）
  - 画像の幅と高さを `struct.pack` でバイナリ化し、区切り文字 `b"<SEP>"` と終端文字 `b"<END>"` を付加して単一のバイト列に結合
  - 名前付き共有メモリ（`"test_memory"`）にバイト列を書き込み、受信側が読み出せるようキー入力待機でメモリを保持

- `process2.py`
  - 受信側プロセスの実装
  - 名前付き共有メモリ（`"test_memory"`）からバイト列を読み込み
  - `b"<END>"` で終端を検出したあと、`b"<SEP>"` で分割して画像バイト列、幅、高さをそれぞれ抽出
  - `struct.unpack` で復元した寸法情報をもとに、`np.frombuffer` と `reshape` で画像配列を復元し、Matplotlib で画面に表示

- `img.png`
  - プロセス間通信のテストで使用する入力画像ファイル

Author: *Gemini 3.8 Flash*


