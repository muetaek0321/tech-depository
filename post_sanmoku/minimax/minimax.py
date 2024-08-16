import random

__all__ = ["minimax_agent"]

# 定数
CHANGE = {
    "X": "O",
    "O": "X"
}


def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()


def check_winner(board, player):
    for row in range(3):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def minimax(board, depth, is_maximizing, turn_p):
    # Check for final state
    if check_winner(board, CHANGE[turn_p]):
        return -10
    if check_winner(board, turn_p):
        return 10
    if all(all(row) for row in board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = turn_p
                    score = minimax(board, depth + 1, False, turn_p)
                    board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = CHANGE[turn_p]
                    score = minimax(board, depth + 1, True, turn_p)
                    board[i][j] = ''
                    best_score = min(score, best_score)
        return best_score


def best_move(board, turn_p):
    best_score = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = turn_p # 'X' ## 
                score = minimax(board, 0, False, turn_p)
                # print((i, j), score)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    move = (i, j)
    # print("----------------------")                
    return move


# def tic_tac_toe():
#     board = [['' for _ in range(3)] for _ in range(3)]
#     current_player = 'O' if random.random() < 0.5 else 'X'

#     while True:
#         print_board(board)
#         if current_player == 'O':
#             row, col = map(int, input('Enter row and column (0, 1, or 2): ').split())
#         else:
#             row, col = best_move(board)

#         board[row][col] = current_player

#         if check_winner(board, current_player):
#             print_board(board)
#             print(f"Player {current_player} wins!")
#             break
#         if all(all(row) for row in board):
#             print_board(board)
#             print("It's a draw!")
#             break

#         current_player = 'O' if current_player == 'X' else 'X'
        

def minimax_agent(board: list, turn_p: str) -> tuple:
    i, j = best_move(board, turn_p)
    
    return i, j


if __name__ == "__main__":
    # tic_tac_toe()
    
    minimax_agent()