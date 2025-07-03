import pygame
from puzzle import *
from pygame.locals import *

w = 800
h = 800

stride_x  = 100
stride_y = 100

def display_console(board):
    screen = pygame.display.set_mode((w, h))
    background = pygame.image.load("./assets/background.png")
    background = pygame.transform.scale(background, (w,h))
    pygame.display.set_caption("Rush Hour Game")
    font = pygame.font.SysFont(None, 32)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        screen.blit(background, (0,0))
        for v in board.vehicles:
            curr_v = board.vehicles[v]
            screen.blit(curr_v.image, (curr_v.pos[0] * stride_x + 100  , curr_v.pos[1] * stride_y + 100)) 
            
        pygame.display.update()
pygame.quit()