import random

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


def player_vs_player():

    board = [" "," "," "," "," "," "," "," "," "]
    current_player = "X"
    print(f"\n----JOUEUR VS JOUEUR----")
    print("Joueur 1 : X, Joueur 2 : O ")
    game_command()

    while True:
        display_board(board)
        print()
        print(f"Tour du joueur {current_player}")   

        while True :
            choice_player = int(input("Enntrer un chiffre entre 1-9 "))
            if not isinstance(choice_player, int):
                print("Veuillez entrer un chiffre svp")
                continue
            
            position = choice_player - 1

            if position < 0 or position > 8 :
                print("Veuillez entrer un nombre entre 1 et 9")
                continue

            if board[position] != " ":
                print("Cette case est déja occupée, prenez une autre \n")
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
            current_player = "O"
        else :
            current_player = "X"




def ai_easy(board, symbol):
    empty_case = get_empty_case(board)
    if empty_case :
        return random.choice(empty_case)
    return False



def ai_hard(board, symbol):
    if symbol == "X":
        next_player = "O"
    else :
        next_player = "X"

    empty_case = get_empty_case(board)
    if not empty_case :
        return False
    
    # Bloquer l'adversaire
    for case in empty_case :
        board_test = board.copy()
        board_test[case] = next_player
        if check_victory(board_test, next_player):
            return case

    # Gagner 
    for case in empty_case:
        board_test = board.copy()
        board_test[case] = symbol
        if check_victory(board_test, symbol):
            return case

    # Jouer au centre
    if board[4] == " ":
        return board[4]
    
    # Jouer les coins
    corners = [0,2,6,8]
    for corner in corners :
        if corner in empty_case:
            return corner
        
    # Jouer les miieux
    middles = [1,3,5,7]
    for middle in middles :
        if middle in empty_case :
            return middle






def main_menu():
    while True:
        print(f"\nMenu Principal du jeu")
        print(f"\n=== Jeu du TicTacToe ===")
        print(f"1. Joueur vs Joueur")
        print(f"2. Quittez")

        choice = int(input(f"\nQuel mode de jeu voulez-vous jouer ? "))
        
        if choice == 1 :
            player_vs_player()

            replay = input("Voulez-vous rejouer ? (o/n) :")
            if replay != "o":
                print("Merci d'avoir joué !")
                break

        elif choice == 2 :
            print("Merci à bientôt")
            break

        else :
            print("Veuillez entrer une option valide")



main_menu()


