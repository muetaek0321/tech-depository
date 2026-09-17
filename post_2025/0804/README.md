### Pythonのデータのキャッシュ保存比較  

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2025/08/04/074500](https://fallpoke-tech.hatenadiary.jp/entry/2025/08/04/074500)

#### 参考URL
- pickle  
[https://qiita.com/hatt0519/items/f1f4c059c28cb1575a93](https://qiita.com/hatt0519/items/f1f4c059c28cb1575a93)  
- shelve  
[https://www.mutable.work/entry/python-shelve](https://www.mutable.work/entry/python-shelve)
- joblib  
[https://note.com/shirotabistudy/n/n3782ae0724e8](https://note.com/shirotabistudy/n/n3782ae0724e8)
- cloudpickle  
[https://note.com/mikiokubo/n/n40d1e068de3a](https://note.com/mikiokubo/n/n40d1e068de3a)

#### ソースコードの説明
`compare_cache_file.ipynb` は、会話データを複数の Python 向けシリアライズ形式でキャッシュ保存し、保存・読み込みにかかる時間や生成ファイルを比較するノートブックです。

- `conversations.json` を UTF-8 の JSON として読み込み、比較対象のデータを用意します。
- `pickle` は `conversations_cache.pickle` にデータを保存し、再度読み込みます。
- `shelve` は `conversations_cache.shelve` を開き、`data` というキーで保存・読み込みます。実行環境によっては `.dat`、`.dir`、`.bak` などの関連ファイルが生成されます。
- `joblib` は圧縮レベル `3` を指定して `conversations_cache.joblib` に保存し、読み込みます。
- `cloudpickle` は `conversations_cache.cloudpickle` に保存し、読み込みます。
- 各保存・読み込み処理には Jupyter の `%%time` マジックを付け、処理時間を計測します。
- `joblib` と `cloudpickle` はノートブック内の `pip install` セルで導入します。

実行には、ノートブックと同じディレクトリに `conversations.json` を配置し、各セルを上から順に実行します。実行結果として、各方式のキャッシュファイルと処理時間が得られます。

Author: *GPT-5.6 Luna（GitHub Copilot）*

