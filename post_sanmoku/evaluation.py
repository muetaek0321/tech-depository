import random

from minimax import minimax_agent
from q_learning import qlearning_agent
from modules import random_agent


def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":  # Check rows
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":  # Check columns
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":  # Check main diagonal
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":  # Check other diagonal
        return board[0][2]
    
    return None


def main():
    # 必要な変数を定義
    # player = minimax_agent
    num_vs = 100
    win_count = 0
    lose_count = 0
    draw_count = 0
    
    # randomのエージェントを作成
    # 乱数固定
    random.seed(0)
    # i, j = random_agent(board)
    
    # 指定回数対戦させる
    # 〇×を割り当て
    # agent = {
    #     "O": minimax_agent,
    #     "X": random_agent
    # }
    
    for num in range(num_vs):
        board = [[""]*3 for _ in range(3)]
        
        # 先攻後攻を決める
        if (num_vs / 2) > num:
            turn = 0
        else:
            turn = 1
        
        # agentを交互に実行
        for _ in range(9):
            if turn == 0:
                turn_p = "O"
                # i, j = minimax_agent(board, turn_p)
                i, j = qlearning_agent(board, turn_p)
                next_p = 1
            elif turn == 1:
                turn_p = "X"
                i, j = random_agent(board)
                next_p = 0
                
            print("turn:", turn, (i, j))
        
            # boardを更新
            board[i][j] = turn_p
        
            # 勝敗が決まっているかどうか確認
            win_p = check_winner(board)
            if win_p is not None:
                print(f"winner({num+1}):", win_p)
                for row in board:
                    print(row)
                
                # 勝利数カウント
                if turn_p == "O":
                    win_count += 1
                elif turn_p == "X":
                    lose_count += 1
                
                break
            
            # # 引き分け判定
            # for row in board:
            #     if "" in row:
            #         # 空いているマスがある（続行）
            #         break
            # else:
            #     # 全て埋まっているが勝者きまらず（対戦終わり）
            #     print("draw")
            #     for row in board:
            #         print(row)
            #     break
                    
        
            # playerを入れ替え
            turn = next_p
            
        else:
            print("draw")
            for row in board:
                print(row)
            draw_count += 1
    
    # 勝率の計算
    win_rate = (win_count / num_vs) * 100
    
    print(f"AIの勝率: {win_rate}%")
    print(f"・勝ち: {win_count} \n・負け: {lose_count} \n・引き分け: {draw_count}")
    
    

if __name__ == "__main__":
    main()