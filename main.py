import random
# faire un score'

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


def check_victory(board, signe):
    # line
    if board[0] == signe and board[1] == signe and board[2] == signe :
        return True
    if board[3] == signe and board[4] == signe and board[5] == signe :
        return True
    if board[6] == signe and board[7] == signe and board[8] == signe :
        return True 
    
    # column
    if board[0] == signe and board[3] == signe and board[6] == signe :
        return True
    if board[1] == signe and board[4] == signe and board[7] == signe :
        return True
    if board[2] == signe and board[5] == signe and board[8] == signe :
        return True
    
    # diagonale
    if board[0] == signe and board[4] == signe and board[8] == signe :
        return True
    if board[2] == signe and board[4] == signe and board[6] == signe :
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




def ai_easy(board, signe):
    empty_case = get_empty_case(board)
    if empty_case :
        return random.choice(empty_case)
    return False



def ai_hard(board, signe):
    if signe == "X":
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
        board_test[case] = signe
        if check_victory(board_test, signe):
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
                player_signe = "X"
                ai_signe = "O"
                player_turn = True
                break

            elif first_player == 2:
                player_signe = "O"
                ai_signe = "X"
                player_turn = False
                break

            else: 
                print("Veuillez entrer soit 1 soit 2")
        except ValueError:
            print("Veuillez entrer un chiffre")
        
    print(f"Vous jouez avec {player_signe}")
    print(f"l'IA joue avec {ai_signe}")
    game_command()

    while True:
        display_board(board)

        if player_turn:
            # TOUR DU JOUEUR
            print(f"Tour du joueur {player_signe}")
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

            board[position] = player_signe
            current_signe = player_signe
            
        else:
            # TOUR DE L'IA
            print(f"Tour de l'IA {level_ai} ")
            position_ai = ai_function(board, ai_signe)
            
            if position_ai is not False:
                board[position_ai] = ai_signe
            else:
                print("Erreur de l'IA")
                break
                
            current_signe = ai_signe

        # Vérifier la VICTORE
        if check_victory(board, current_signe):
            display_board(board)
            if current_signe == player_signe:
                print(f"Bravo, vous avez gagné contre l'IA {level_ai} !")
            else:
                print(f"L'IA {level_ai} a gagné !")
            break

        # Vérifier MATCH NUL
        if board_full(board):
            display_board(board)
            print(" Match nul !")
            break

        # Changer de tour
        player_turn = not player_turn


def ia_vs_ia():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print("\n----IA VS IA----")
    print("\nChoisir le niveau de l'IA 1")
    print("1. Mode Facile")
    print("2. Mode Difficile")

    while True:
        try:
            choice_ai1 = int(input("Entrer votre choix 1-2 : "))
            if choice_ai1 == 1:
                ai1_function = ai_easy
                level_ai1 = "facile"
                break

            elif choice_ai1 == 2:
                ai1_function = ai_hard
                level_ai1 = "difficile"
                break

            else: 
                print("Veuillez entrer soit 1 ou 2 : ")

        except ValueError:
            print("Veuillez entre un chiffre")

    print("\nChoisir le niveau de l'IA 2")
    print("1. Mode Facile")
    print("2. Mode Difficile")

    while True:
        try:
            choice_ai2 = int(input("Entrer votre choix 1-2 : "))
            if choice_ai2 == 1:
                ai2_function = ai_easy
                level_ai2 = "facile"
                break

            elif choice_ai2 == 2:
                ai2_function = ai_hard
                level_ai2 = "difficile"
                break

            else: 
                print("Veuillez entrer soit 1 ou 2 : ")

        except ValueError:
            print("Veuillez entre un chiffre")
    
    print("\nLe match débute")

    turn_ai1 = True
    while True :
        display_board(board)
        print("Debut du jeu, appuyer pour debuter le match")

        if turn_ai1 :
            print(f"Tour de l'IA 1 ({level_ai1})")
            print(f"Le signee de l'IA 1 est X")
            position = ai1_function(board, "X")

            if position is not False:
                board[position] = "X"
                current_signe = "X"
            else : 
                print("Erreur IA 1 !")
                break

        else :
            # Tour IA 2
            print(f"Tour de l'IA 2 ({level_ai2})")
            print(f"Le signee de l'IA 1 est O")
            position = ai2_function(board, "O")

            if position is not False:
                board[position] = "O"
                current_signe = "O"
            else : 
                print("Erreur IA 2 !")
                break
        
        if check_victory(board, current_signe):
            display_board(board)
            if turn_ai1:
                print(f"L'IA 1 ({level_ai1}) a gagné")
            else:
                print(f"L'IA 2 ({level_ai2}) a gagné")
            break

        if board_full(board):
            display_board(board)
            print("Match nul")
            break

        # Changer de tour
        turn_ai1 = not turn_ai1
        # Control des tours
        input("Appuyer sur entrer pour continuer :  ")



def main_menu():
    while True:
        print(f"\nMenu Principal du jeu")
        print(f"\n=== Jeu du TicTacToe ===")
        print(f"1. Joueur VS Joueur")
        print(f"2. Joueur VS IA")
        print(f"3. IA VS IA")
        print(f"4. Quittez")

        choice = int(input(f"\nQuel mode de jeu voulez-vous jouer ? "))
        
        if choice == 1 :
            player_vs_player()
        
        elif choice == 2 :
            player_vs_ai()

        elif choice == 3 :
            ia_vs_ia()

        elif choice == 4 :
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


    
