"""
文字コードがutf-8とshift-jisのファイルを作成するためのプログラム
"""

text = "テスト用のファイルです。"

# utf-8のファイルを作成
with open("utf8_file.txt", "w", encoding="utf-8") as f:
    f.write(text)

# shift-jisのファイルを作成
with open("shift_jis_file.txt", "w", encoding="shift_jis") as f:
    f.write(text)

