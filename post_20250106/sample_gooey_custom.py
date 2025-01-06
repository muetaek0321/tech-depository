"""
日本語化、windowの設定、簡単なレイアウト変更
"""
from gooey import Gooey, GooeyParser


@Gooey(
    default_size=(800, 800), # 表示した際のウィンドウサイズ
    language="japanese", # 言語の指定
    language_dir="./languages" # 言語ファイルの参照先
)
def main() -> None:
    parser = GooeyParser(description="サンプルプログラムです。")

    main_params = parser.add_argument_group("パラメータ")
    main_params.add_argument("number", type=int, help='数値を入力')
    main_params.add_argument("-s", "--string", type=str, default="サンプル文字列", help='文字列を入力')
    main_params.add_argument("--flag", action='store_true')
    
    sub_params = parser.add_argument_group("オプション")
    sub_params.add_argument("--choice", default="Google", choices=['Google', 'Apple', 'Facebook', 'Amazon'])
    sub_params.add_argument("--list", nargs='*', 
                            choices=['Microsoft', 'Amazon', 'Tesla', 'Alphabet', 'NVIDIA', 'Apple'])

    args = parser.parse_args()  

    print("number", args.number)
    print("string", args.string)
    print("flag", args.flag)
    print("choice", args.choice)
    print("list", args.list)

if __name__ == "__main__":
    main()