import json
import re
import unicodedata
from collections import Counter

from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def main() -> None:
    # conversations.jsonを読み込み
    json_path = "./conversations.json"
    with open(json_path, mode='r', encoding='utf-8') as f:
        json_contents = json.load(f)
    
    # ユーザの入力内容のみを取得
    text = ""
    for json_content in json_contents:
        for chat_id in json_content["mapping"].keys():
            if json_content["mapping"][chat_id]["message"]:
                message = json_content["mapping"][chat_id]["message"]
                if message["author"]["role"] == "user":
                    part = message["content"]["parts"][0]
                    if isinstance(part, str):
                        text += part
    
    # 正規表現を使った文字列の削除
    text = re.sub(r"[^\w\s\u3000-\u9FFF]", "", text, flags=re.UNICODE)
    # 文字列の正規化
    text_norm = unicodedata.normalize('NFKC', text)
    
    # 文書のtoken化（janomeで分かち書きする）
    t = Tokenizer()
    tokenized_text = t.tokenize(text_norm)

    # 文字列のうち名詞のみを抽出
    words_list=[]
    for token in tokenized_text:
        tokenized_word = token.surface
        hinshi = token.part_of_speech.split(',')[0]
        hinshi2 = token.part_of_speech.split(',')[1]
        if hinshi == "名詞":
            if (hinshi2 != "数") and (hinshi2 != "代名詞") and (hinshi2 != "非自立"):
                words_list.append(tokenized_word)
    
    # 抽出した単語のリストをスペース区切りの文字列に変換
    words_wakachi = " ".join(words_list)
    
    # 頻出単語を確認
    for word_count in Counter(words_list).most_common():
        print(word_count)
    
    # ストップワードの設定
    stopwords = ["_", "u"]
    
    # WordCloudを作成
    word_cloud = WordCloud(
        font_path=r"C:\Windows\Fonts\BIZ-UDGOTHICB.TTC", 
        width=1500, height=900, stopwords=set(stopwords),
        min_font_size=5, collocations=False, background_color='white', max_words=400
    )
    word_cloud_img = word_cloud.generate(words_wakachi)
    
    # 表示
    figure = plt.figure(figsize=(15, 10))
    plt.imshow(word_cloud_img)
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.xticks([])
    plt.yticks([])
    plt.show()
    figure.savefig("wordcloud.png")


if __name__ == "__main__": 
    main()

