import configparser

import pandas as pd

from .utils import get_ql_action


# 定数
PLAY_AREA_TO_BOARD = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                      4: (1, 0), 5: (1, 1), 6: (1, 2),
                      7: (2, 0), 8: (2, 1), 9: (2, 2)}


def board_to_play_area(board: list) -> list:
    """boardをQ学習の仕様に合わせて変換
    """
    # play_areaの初期化
    play_area = list(range(1, 10))
    
    # boardを1行のデータに変換
    board_flat = board[0] + board[1] + board[2]
    
    # boardの"O","X"をplay_areaに書き込み
    for i, b in enumerate(board_flat):
        if b != "":
            play_area[i] = b

    return play_area    


def qlearning_agent(
    board: list, 
    turn_p: str = "O",
) -> tuple:
    """Q学習で三目並べを実行する対戦エージェント
    
    Args:
        board (list): 盤面の状態を格納したリスト
        turn_p (str): 現在選択中のプレイヤー
    """
    # コンフィグファイルの読み込み
    cfg = configparser.ConfigParser()
    cfg.read('./q_learning/config.ini', encoding='utf-8')
    if turn_p == "O":
        weight_file = cfg["AGENT"]["p1_weight"]
    elif turn_p == "X":
        weight_file = cfg["AGENT"]["p2_weight"]

    # 重みファイルの読み込んでQテーブルを設定
    q_table = pd.read_csv(weight_file, header=None).to_numpy()
    
    # boardの形式をQ学習のコードに合わせて変換
    play_area = board_to_play_area(board)
    # print(play_area)
    # return
    
    # AI判定を実行
    choosable_area = [str(area) for area in play_area if type(area) is int]
    ai_input = get_ql_action(play_area, choosable_area, q_table, epsilon=0)
    
    # 入力位置を元のboardの座標位置に変換
    i, j = PLAY_AREA_TO_BOARD[ai_input]
    
    return i, j
    
if __name__ == "__main__":
    board = [["X", "", "X"], 
             ["", "O", ""], 
             ["", "", ""]]
    for row in board:
        print(row)
    i, j = qlearning_agent(board, "O")
    
    print(i, j)
