from argparse import ArgumentParser

from gooey import Gooey


@Gooey
def main() -> None:
    parser = ArgumentParser(description="サンプルプログラムです。")

    parser.add_argument("number", type=int, help='数値を入力')
    parser.add_argument("-s", "--string", type=str, default="サンプル文字列", help='文字列を入力')
    parser.add_argument("--flag", action='store_true')    
    parser.add_argument("--choice", default="Google", choices=['Google', 'Apple', 'Facebook', 'Amazon'])
    parser.add_argument("--list", nargs='*', 
                        choices=['Microsoft', 'Amazon', 'Tesla', 'Alphabet', 'NVIDIA', 'Apple'])

    args = parser.parse_args()  

    print("number", args.number)
    print("string", args.string)
    print("flag", args.flag)
    print("choice", args.choice)
    print("list", args.list)

if __name__ == "__main__":
    main()