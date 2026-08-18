### WordCloudでChatGPTの履歴を解析 

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2025/08/15/221947](https://fallpoke-tech.hatenadiary.jp/entry/2025/08/15/221947)


#### 参考サイト  
[https://qiita.com/Mikeinu/items/dd5e9af26fd3a5f3c8e0](https://qiita.com/Mikeinu/items/dd5e9af26fd3a5f3c8e0)


#### ソースコードの説明

`wordcloud_chatgpt_history.py` は、ChatGPTからエクスポートされた会話履歴ファイル（`conversations.json`）を解析し、ユーザーの発言データから名詞を抽出してWordCloud（ワードクラウド）画像を出力するスクリプトです。

##### 主な処理フロー
1. **データ読み込み・テキスト抽出**:
   - `conversations.json` を読み込み、`role == "user"` の発言テキストのみを集計します。
2. **テキストの整形・正規化**:
   - 正規表現を用いて不要な記号を除去し、`unicodedata.normalize('NFKC', ...)` で全角・半角等の文字正規化を行います。
3. **形態素解析（Janome）**:
   - Janomeの `Tokenizer` を使用してテキストを分かち書きし、品詞判定により「数」「代名詞」「非自立」を除く名詞のみを抽出します。
4. **出現単語の集計・WordCloud生成**:
   - `Counter` を用いて単語の頻度を出力します。
   - 日本語フォント（`BIZ-UDGOTHICB.TTC`）やストップワードを設定し、WordCloud を生成します。
5. **描画・画像保存**:
   - Matplotlib を使って描画し、`wordcloud.png` として画像ファイルに保存します。

##### 依存関係・主要ライブラリ
- **標準ライブラリ**: `json`, `re`, `unicodedata`, `collections`
- **外部ライブラリ**: `janome`, `wordcloud`, `matplotlib`

*Author: Gemini 3.6 Flash*

