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

def get_empty_case(board):
    empty_case = []
    for i in range(9):
        if board[i] == " ":
            empty_case.append(i)
    return empty_case


def player_vs_player(board,symbol):

    board = [" "," "," "," "," "," "," "," "," "]
    current_player = "X"
    print("----MODE DEUX JOUEURS----")
    print("Joueur 1 : X, Joueur 2 : O ")
    game_command()

    while True:
        display_board(board)
        print()
        print(f"Tour du joueur {current_player}")   

        while True :
            choice_player = int(input("Enter a number between 1-9"))
            if not isinstance(choice_player, int):
                print("Veuillez entrer un chiffre svp")
                continue
            
            position = choice_player - 1

            if position < 0 and position > 8 :
                print("Veuillez entrer un nombre entre 1 et 9")
                continue

            break

        board[position] = current_player

        # Victory
        if check_victory(board, current_player):
            display_board(board)
            print(f"Le joueur {current_player} a gagné ! BRAVO ")
            break

        # Draw
        if board_full(board):
            display_board(board)
            print(f"La table de jeu est plein, match nul !!!")
            break


        # Change player
        if current_player == "X" :
            current_player == "O"
        else :
            current_player == "O"




            





        
        



