import subprocess

def execute_command(command) -> None:
    """subprocessを使用してコマンドを実行し、その出力を返します。
    """
    try:
        # コマンドを実行します
        result = subprocess.run(
            command, capture_output=True, text=True, 
            check=True, encoding='utf-8', shell=True 
        )
        print("--- 出力 ---")
        print(result.stdout)

    except FileNotFoundError:
        print(f"エラー: コマンド '{command}' が見つかりませんでした。")
        
    except subprocess.CalledProcessError as e:
        print(f"コマンド実行エラー: {command}")
        print(f"リターンコード: {e.returncode}")
        print("--- 標準出力 ---")
        print(e.stdout)
        print("--- 標準エラー出力 ---")
        print(e.stderr)
        
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")


def main() -> None:
    target = "execute_gemini.py"
    
    # プロンプトを読み込み
    with open("./prompt2.txt", mode="r", encoding="cp932") as f:
        prompt_text = f.read()
        
    # パスの指定を埋め込み
    prompt_text = prompt_text.format(target=target)
    # 改行を除く（改行コードまでの文字列しか参照されないため）
    prompt_text = prompt_text.replace("\n", "")
    
    print("--- 入力 ---")
    print(prompt_text)
    
    # 実行するCLIコマンド
    command = ["gemini", "--prompt", prompt_text]
    
    # コマンド実行
    execute_command(command)


if __name__ == "__main__":
    main()