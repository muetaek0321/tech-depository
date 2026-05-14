---
name: generate_readme
tools: [vscode, execute, read, agent, edit, search, web, browser, 'gitkraken/*', todo]
description: READMEのソースコード説明を自動で記載するプロンプト
---

指定されたディレクトリ配下のソースコードを解析し、
同じ階層にある README.md にソースコードの説明を追記してください。

# 対象

- 指定されたディレクトリ直下のコード
- 必要に応じてサブディレクトリも参照
- import / dependency 関係も考慮

# 条件

- 対象ディレクトリをチャットで指定
- 既に作成されたREADME.mdにある`#### ソースコードの説明`以下に生成した内容を追記
