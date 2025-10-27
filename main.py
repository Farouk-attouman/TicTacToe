def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print(f"---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print(f"---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")

def game_command():
    print("Touches du jeu : ")
    print(" 1 | 2 | 3")
    print("---|---|---")
    print(" 4 | 5 | 6")
    print("---|---|---")
    print(" 7 | 8 | 9")



def check_victory(board, symbol):
    # line
    if board[0] == symbol and board[1] == symbol and board[2] == symbol :
        return True
    if board[3] == symbol and board[4] == symbol and board[5] == symbol :
        return True
    if board[6] == symbol and board[7] == symbol and board[8] == symbol :
        return True 
    
    # column
    if board[0] == symbol and board[3] == symbol and board[6] == symbol :
        return True
    if board[1] == symbol and board[4] == symbol and board[7] == symbol :
        return True
    if board[2] == symbol and board[5] == symbol and board[8] == symbol :
        return True
    
    # diagonale
    if board[0] == symbol and board[4] == symbol and board[8] == symbol :
        return True
    if board[2] == symbol and board[4] == symbol and board[6] == symbol :
        return True
    
    return False

def board_full(board):
    for case in board:
        if case == " " :
            return False
    return True
          
           