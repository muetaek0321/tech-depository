
ブログ記事はこちら↓<br>
[https://fallpoke-tech.hatenadiary.jp/entry/2024/09/16/182637](https://fallpoke-tech.hatenadiary.jp/entry/2024/09/16/182637)<br>

関数**trans_and_show_image**の引数にAlbumentationsの処理のリストを渡すことで使用できます。
```Python
trans_and_show_image([
    # ここに適用したい処理を書く
    A.Flip()
    A.BBoxSafeRandomCrop()
    A.Resize(height=512, width=512)
])
```
