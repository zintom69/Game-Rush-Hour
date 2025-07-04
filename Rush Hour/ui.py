import pygame
from pygame.locals import QUIT
from puzzle import Board

pygame.init() 
w = 800
h = 800
stride_x  = 100
stride_y = 100
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Rush Hour Game")

def display_console(board):
    global screen
    # font = pygame.font.SysFont(None, 32)
    # running = True
    delay_time = 0

    # while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    background = pygame.image.load("./assets/background.png")
    background = pygame.transform.scale(background, (w,h))
    screen.blit(background, (0,0))
    
    for v in board.vehicles:
        curr_v = board.vehicles[v]
        screen.blit(curr_v.image, (curr_v.pos[0] * stride_x + 100  , curr_v.pos[1] * stride_y + 100))
    
    pygame.display.update()
    pygame.time.delay(delay_time)

def display_console_goal(board):
    global screen
    # font = pygame.font.SysFont(None, 32)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        background = pygame.image.load("./assets/background.png")
        background = pygame.transform.scale(background, (w,h))
        screen.blit(background, (0,0))
    
        for v in board.vehicles:
            curr_v = board.vehicles[v]
            screen.blit(curr_v.image, (curr_v.pos[0] * stride_x + 100  , curr_v.pos[1] * stride_y + 100))
        pygame.display.update()
    pygame.quit()
    exit()