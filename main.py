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
        return 4
    
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
        

def player_vs_ai():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print("\n----JOUEUR VS IA----")
    print("\nChoisir le niveau de l'IA")
    print("1. Mode Facile")
    print("2. Mode Difficile")

    while True:
        try:
            choice = int(input("Entrer votre choix 1-2 : "))
            if choice == 1:
                ai_function = ai_easy
                level_ai = "facile"
                break

            elif choice == 2:
                ai_function = ai_hard
                level_ai = "difficile"
                break

            else: 
                print("Veuillez entrer soit 1 ou 2 : ")

        except ValueError:
            print("Veuillez entre un chiffre")
    
    print("\nQui joue en premier")
    print("1. Joueur")
    print("2. IA")

    while True:
        try: 
            first_player = int(input("entrer votre choix 1-2 : "))

            if first_player == 1:
                player_symbol = "X"
                ai_symbol = "O"
                player_turn = True
                break

            elif first_player == 2:
                player_symbol = "O"
                ai_symbol = "X"
                player_turn = False
                break

            else: 
                print("Veuillez entrer soit 1 soit 2")
        except ValueError:
            print("Veuillez entrer un chiffre")
        
    print(f"Vous jouez avec {player_symbol}")
    print(f"l'IA joue avec {ai_symbol}")
    game_command()

    while True:
        display_board(board)

        if player_turn:
            # TOUR DU JOUEUR
            print(f"Tour du joueur {player_symbol}")
            while True:
                try:
                    player_choice = int(input("Entrer un chiffre entre 1-9 : "))
                    position = player_choice - 1

                    if position < 0 or position > 8:
                        print("Veuillez entrer un chiffre entre 1 et 9 : ")
                        continue

                    if board[position] != " ":
                        print("Cette case est déjà occupée")
                        continue

                    break
                except ValueError:
                    print("Veuillez entrez un chiffre svp")

            board[position] = player_symbol
            current_symbol = player_symbol
            
        else:
            # TOUR DE L'IA
            print(f"Tour de l'IA {level_ai} ")
            position_ai = ai_function(board, ai_symbol)
            
            if position_ai is not False:
                board[position_ai] = ai_symbol
            else:
                print("Erreur de l'IA")
                break
                
            current_symbol = ai_symbol

        # Vérifier la VICTORE
        if check_victory(board, current_symbol):
            display_board(board)
            if current_symbol == player_symbol:
                print(f"Bravo, vous avez gagné contre l'IA {level_ai} !")
            else:
                print(f"L'IA {level_ai} a gagné !")
            break

        # Vérifier MATCH NUL
        if board_full(board):
            display_board(board)
            print("🤝 Match nul !")
            break

        # Changer de tour
        player_turn = not player_turn


def main_menu():
    while True:
        print(f"\nMenu Principal du jeu")
        print(f"\n=== Jeu du TicTacToe ===")
        print(f"1. Joueur vs Joueur")
        print(f"2. Joueur vs IA")
        print(f"3. Quittez")

        choice = int(input(f"\nQuel mode de jeu voulez-vous jouer ? "))
        
        if choice == 1 :
            player_vs_player()
        
        elif choice == 2 :
            player_vs_ai()

        elif choice == 3 :
            print("Merci à bientôt")
            break

        else :
            print("Veuillez entrer une option valide")
            continue

        replay = input("Voulez-vous rejouer ? (o/n) :")
        if replay.lower() != "o":
            print("Merci d'avoir joué !")
            break



main_menu()


    
