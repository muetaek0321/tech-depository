### チャットベースでさらにMCPサーバを試す回【LangChain MCP Adapters】

### 記事
[https://fallpoke-tech.hatenadiary.jp/entry/2025/06/13/002736](https://fallpoke-tech.hatenadiary.jp/entry/2025/06/13/002736)

#### 実行コマンド

```bash
uv run python response_gemini_mcp.py --config config/mcp_config_fetch.json
```
または
```bash
uv run python response_gemini_mcp.py --config config/mcp_config_git.json
```

#### ソースコードの説明

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9?logo=astral&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?logo=googlegemini&logoColor=white)

このディレクトリは、LangChain と `langchain-mcp-adapters` を利用して、Gemini モデルから Model Context Protocol (MCP) サーバーの各種ツールを呼び出し、対話形式でタスクを実行するデモコードです。設定ファイルを切り替えることで、Webコンテンツ取得（fetch）や Git 操作（git）など異なる MCP サーバーと連携可能です。

- `response_gemini_mcp.py`
  - コマンドライン引数（`--config`）で指定された設定ファイルから MCP サーバー構成を読み込み、LangChain の `MultiServerMCPClient` を用いてツール群を取得
  - `ChatGoogleGenerativeAI`（Gemini 2.5 Flash Preview）および `create_tool_calling_agent` / `AgentExecutor` を使ってツール呼び出しエージェントを構築
  - 対話形式でユーザーからの質問（`user_input`）を受け取り、MCP ツールを活用して非同期（`asyncio`）で回答を生成・出力

- `config/mcp_config_fetch.json`
  - Web ページ等のコンテンツ取得用 MCP サーバー（`uvx mcp-server-fetch`）を `stdio` 経由で接続するための設定ファイル

- `config/mcp_config_git.json`
  - Git リポジトリ操作用 MCP サーバー（`uvx mcp-server-git`）を `stdio` 経由で接続するための設定ファイル

- `pyproject.toml`
  - プロジェクト設定および依存パッケージ（Python 3.12 以上、`langchain`、`langchain-google-genai`、`langchain-mcp-adapters`）の定義

Author: *Gemini 3.8 Flash*
