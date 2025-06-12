import asyncio
import json
from argparse import ArgumentParser
from pathlib import Path

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_tool_calling_agent, AgentExecutor


# 定数
TEMPLATE = """
あなたは質問応答タスクのアシスタントです。
登録されているツールを使って質問に答えてください。

質問: {question}
答え: {agent_scratchpad}
"""

# AIの返答を作成
async def gemini_mcp_generator(user_input, mcp_config_path):        
    # モデルを準備
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-05-20")
    # プロンプトを設定
    prompt = PromptTemplate.from_template(TEMPLATE)
    
    with open(mcp_config_path, mode="r") as f:
        mcp_config = json.load(f)
    
    mcp_client = MultiServerMCPClient(mcp_config["mcpServers"])
    tools = await mcp_client.get_tools()
    
    # エージェントを用意
    agent = create_tool_calling_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools)
    
    # 返答を取得
    response = await executor.ainvoke({"question": user_input})
    
    print("\n返答：\n")
    print(response["output"])
    
    
if __name__ == "__main__":
    # コマンドライン引数の設定
    parser = ArgumentParser()
    parser.add_argument("--config", type=str)
    args = parser.parse_args()
    
    # 単体テスト
    mcp_config_path = Path(args.config)
    
    # コマンドラインから入力
    user_input = input("質問を入力 >>> ")
    
    asyncio.run(gemini_mcp_generator(user_input, mcp_config_path))