"""
デフォルトの文字コードの変更を確認するためのプログラム
実行前に「set PYTHONUTF8=1」をコマンドプロンプトで実行しておくとエラーなく実行可能
"""
# import os
# os.environ["PYTHONUTF8"] = "1"

# with open("./shift_jis_file.txt", "r") as f:
#     content = f.read()
# print("shift_jis_file.txt: OK")

with open("./utf8_file.txt", "r") as f:
    content = f.read()
print("utf8_file.txt: OK")
