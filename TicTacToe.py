import pygame

pygame.init()

# Dimension
width = 600
height = 600
screen = pygame.display.set_mode((width, height))

grid = []
for i in range(3):
    grid.append([" ", " ", " "]) 

# Current player
player = "X"

# Police
police = pygame.font.Font(None, 100)

def draw_grid():
    screen.fill((255, 255, 255))
    # lignes
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), 5)
    # colonnes
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 200), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), 5)

def draw_symbol():
    for line in range(3):
        for column in range(3):
            if grid[line][column] == "X":
                text = police.render("X", True, (0, 0, 0))
                screen.blit(text, (column * 200 + 60, line * 200 + 50))
            elif grid[line][column] == "O":
                text = police.render("O", True, (0, 0, 0))
                screen.blit(text, (column * 200 + 60, line * 200 + 50))

def check_victory():
    # Lignes
    for line in range(3):
        if grid[line][0] == grid[line][1] == grid[line][2] != " ":
            return True    
    # Colonnes
    for column in range(3):
        if grid[0][column] == grid[1][column] == grid[2][column] != " ":
            return True 
    # Diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] != " ":
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] != " ":
        return True
    return False

def grid_full():
    for line in range(3):
        for column in range(3):
            if grid[line][column] == " ":
                return False
    return True

def show_message(message):
    caractere = pygame.font.Font(None, 60)
    text = caractere.render(message, True, (0, 0, 0))
    rect = text.get_rect(center=(300, 300))
    pygame.draw.rect(screen, (255, 255, 255), (50, 250, 500, 100))
    pygame.draw.rect(screen, (0, 0, 0), (50, 250, 500, 100), 3)
    screen.blit(text, rect)

# Boucle du jeu
clock = pygame.time.Clock()
running = True
game_over = False
message = ""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            line = y // 200  
            column = x // 200
            
            # Mettre un symbole si vide
            if grid[line][column] == " ":
                grid[line][column] = player
                
                # Vérifier victoire
                if check_victory():
                    game_over = True
                    message = f"Joueur {player} a gagné"
                elif grid_full():
                    game_over = True
                    message = "Match nul"
                else:
                    # Changer de joueur
                    player = "O" if player == "X" else "X"
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                grid = []
                for i in range(3):
                    grid.append([" ", " ", " "])
                player = "X"
                game_over = False
    
    # Dessin
    draw_grid()
    draw_symbol()
    
    if game_over:
        show_message(message)
        caractere = pygame.font.Font(None, 30)
        replay = caractere.render("Appuyez sur R pour rejouer", True, (0, 0, 0))
        screen.blit(replay, (150, 500))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()