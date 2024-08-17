import random


def random_agent(
    board: list,
) -> tuple:
    """ランダムで盤面を選択するエージェント
    
    Args:
        board (list): 盤面の状態を格納したリスト
    """
    # boardの状態を確認
    blank_state_list = []
    for i, row in enumerate(board):
        for j, state in enumerate(row):
            if state == "":
                blank_state_list.append((i, j))
                
    # 〇×が入っていないマスをランダムに選択
    choice = random.choice(blank_state_list)
    
    return choice

