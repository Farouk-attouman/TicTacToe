import pygame
import sys

pygame.init()

#Dimension
width = 600
height = 600
screen = pygame.display.set_mode((width,height))

#Grid
grid =[]
for i in range(3):
    grid.append(["","",""])

#Current player
player = "X"

#Police
police = pygame.font.Font(None,100)

def draw_grid():
    screen.fill(255,255,255)
    #line
    pygame.draw.line(screen,(0,0,0),(200,0),(200,600),5)
    pygame.draw.line(screen,(0,0,0),(400,0),(400,600),5)
    #column
    pygame.draw.line(screen,(0,0,0),(0,200),(600,200),5)
    pygame.draw.line(screen,(0,0,0),(0,400),(600,400),5)

def draw_symbol():
    for line in range(3):
        for column in range(3):
            if grid[line][column] == "X":
                text = police.render("X", True, (0,0,0))
                screen.blit(text, (column*200 + 60, line*200 + 50))
            elif grid[line][column] == "O":
                text = police.render("0", True, (0,0,0))
                screen.blit(text, (column*200 + 60, line*200 + 50))

def check_victory():
    # line
    for line in range(3):
        if grid[line][0] == grid[line][1] == grid[line][2] != " ":
            return True    
    # column
    for column in range(3):
        if grid[0][column] == grid[1][column] == grid[2][column] != " ":
            return True 
    # diagonale
    if grid[0][0] == grid[1][1] == grid[2][2] != " ":
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] != " ":
        return True
    
    return False

