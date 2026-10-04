### PythonからGeminiCLIを動作させるサンプル 

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2025/07/14/074500](https://fallpoke-tech.hatenadiary.jp/entry/2025/07/14/074500)

#### プロジェクト概要

このディレクトリには、Geminiとの対話やプロンプトに関するファイルが含まれています。

#### ソースコードの説明

このディレクトリは、Python の `subprocess` モジュールを介して Gemini CLI を呼び出し、指定したプロンプトを渡して応答を取得するサンプル実装である。

- `execute_gemini.py`
  - `execute_command(command)` 関数：`subprocess.run` でシェルコマンドを実行し、標準出力を表示する。`FileNotFoundError`・`CalledProcessError`・汎用 `Exception` の3段階でエラーハンドリングしており、失敗時はリターンコードと標準エラー出力も出力する。`shell=True`・`encoding='utf-8'` を指定。
  - `main()` 関数：`prompt2.txt` を `cp932` で読み込み、`{target}` プレースホルダーに対象ファイル名（`execute_gemini.py`）を埋め込む。改行をすべて除去したうえで `gemini --prompt <テキスト>` の形でコマンドを組み立て、`execute_command` に渡す。
  - 標準ライブラリのみを使用（`subprocess`）。

- `prompt.txt`
  - Gemini CLI へのプロンプトの雛形が記述されたテキストファイル（Shift-JIS / cp932 エンコード）。`{target}` プレースホルダーを含み、`main()` 内で実行時に対象ファイルパスへ置換される。

- `prompt2.txt`
  - `execute_gemini.py` の `main()` から実際に読み込まれるプロンプトファイル（cp932 エンコード）。カレントフォルダのファイルを参照して README.md を生成・出力するよう Gemini に指示する内容が記述されている。改行は `main()` 内でスペースなしに除去されてからコマンドへ渡される。

Author: *Claude Sonnet 4.6*