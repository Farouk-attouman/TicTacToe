import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
largeur = 600
hauteur = 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Tic-Tac-Toe")

# Grille du jeu (3x3)
grille = [['' for _ in range(3)] for _ in range(3)]

# Joueur actuel
joueur = 'X'

# Police pour le texte
police = pygame.font.Font(None, 100)

def dessiner_grille():
    fenetre.fill((255, 255, 255))
    # Lignes verticales
    pygame.draw.line(fenetre, (0, 0, 0), (200, 0), (200, 600), 5)
    pygame.draw.line(fenetre, (0, 0, 0), (400, 0), (400, 600), 5)
    # Lignes horizontales
    pygame.draw.line(fenetre, (0, 0, 0), (0, 200), (600, 200), 5)
    pygame.draw.line(fenetre, (0, 0, 0), (0, 400), (600, 400), 5)

def dessiner_symboles():
    for ligne in range(3):
        for colonne in range(3):
            if grille[ligne][colonne] == 'X':
                texte = police.render('X', True, (0, 0, 0))
                fenetre.blit(texte, (colonne * 200 + 60, ligne * 200 + 50))
            elif grille[ligne][colonne] == 'O':
                texte = police.render('O', True, (0, 0, 0))
                fenetre.blit(texte, (colonne * 200 + 60, ligne * 200 + 50))

def verifier_victoire():
    # Vérifier les lignes
    for ligne in range(3):
        if grille[ligne][0] == grille[ligne][1] == grille[ligne][2] != '':
            return True
    
    # Vérifier les colonnes
    for colonne in range(3):
        if grille[0][colonne] == grille[1][colonne] == grille[2][colonne] != '':
            return True
    
    # Vérifier les diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] != '':
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] != '':
        return True
    
    return False

def grille_pleine():
    for ligne in range(3):
        for colonne in range(3):
            if grille[ligne][colonne] == '':
                return False
    return True

def afficher_message(message):
    fonte = pygame.font.Font(None, 60)
    texte = fonte.render(message, True, (0, 0, 0))
    rect = texte.get_rect(center=(300, 300))
    pygame.draw.rect(fenetre, (255, 255, 255), (50, 250, 500, 100))
    pygame.draw.rect(fenetre, (0, 0, 0), (50, 250, 500, 100), 3)
    fenetre.blit(texte, rect)

# Boucle principale du jeu
jeu_termine = False
horloge = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not jeu_termine:
            x, y = pygame.mouse.get_pos()
            colonne = x // 200
            ligne = y // 200
            
            # Placer le symbole si la case est vide
            if grille[ligne][colonne] == '':
                grille[ligne][colonne] = joueur
                
                # Vérifier si quelqu'un a gagné
                if verifier_victoire():
                    jeu_termine = True
                    message_gagnant = f"Joueur {joueur} a gagné!"
                elif grille_pleine():
                    jeu_termine = True
                    message_gagnant = "Match nul!"
                else:
                    # Changer de joueur
                    joueur = 'O' if joueur == 'X' else 'X'
        
        # Recommencer le jeu avec la touche R
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                grille = [['' for _ in range(3)] for _ in range(3)]
                joueur = 'X'
                jeu_termine = False
    
    # Dessiner tout
    dessiner_grille()
    dessiner_symboles()
    
    if jeu_termine:
        afficher_message(message_gagnant)
        fonte_petit = pygame.font.Font(None, 30)
        texte_rejouer = fonte_petit.render("Appuyez sur R pour rejouer", True, (0, 0, 0))
        fenetre.blit(texte_rejouer, (150, 500))
    
    pygame.display.flip()
    horloge.tick(60)