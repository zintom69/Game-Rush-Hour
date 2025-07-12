import pygame
from puzzle import *
from pygame.locals import *
from button import Button

w = 1200
h = 675

w_board = w//2
scale_board = w_board*100//800
stride_x  = scale_board
stride_y = scale_board
x_pos_board = 500

# Image for button
play_btn_img = pygame.image.load("./assets/ControlButtons/Play.png")
reset_btn_img = pygame.image.load("./assets/ControlButtons/Reset.png")
pause_btn_img = pygame.image.load("./assets/ControlButtons/Pause.png")

background_map_img = pygame.image.load("./assets/MapButtons/Maps.png")
background_alg_img = pygame.image.load("./assets/AlgorithmButtons/Algorithms.png")

# Load map buttons images
map1_d = pygame.image.load("./assets/MapButtons/1(A).png")
map1_s = pygame.image.load("./assets/MapButtons/1(B).png")
map2_d = pygame.image.load("./assets/MapButtons/2(A).png")
map2_s = pygame.image.load("./assets/MapButtons/2(B).png")
map3_d = pygame.image.load("./assets/MapButtons/3(A).png")
map3_s = pygame.image.load("./assets/MapButtons/3(B).png")
map4_d = pygame.image.load("./assets/MapButtons/4(A).png")
map4_s = pygame.image.load("./assets/MapButtons/4(B).png")
map5_d = pygame.image.load("./assets/MapButtons/5(A).png")
map5_s = pygame.image.load("./assets/MapButtons/5(B).png")
map6_d = pygame.image.load("./assets/MapButtons/6(A).png")
map6_s = pygame.image.load("./assets/MapButtons/6(B).png")
map7_d = pygame.image.load("./assets/MapButtons/7(A).png")
map7_s = pygame.image.load("./assets/MapButtons/7(B).png")
map8_d = pygame.image.load("./assets/MapButtons/8(A).png")
map8_s = pygame.image.load("./assets/MapButtons/8(B).png")
map9_d = pygame.image.load("./assets/MapButtons/9(A).png")
map9_s = pygame.image.load("./assets/MapButtons/9(B).png")
map10_d = pygame.image.load("./assets/MapButtons/10(A).png")
map10_s = pygame.image.load("./assets/MapButtons/10(B).png")
map11_d = pygame.image.load("./assets/MapButtons/11(A).png")
map11_s = pygame.image.load("./assets/MapButtons/11(B).png")
map12_d = pygame.image.load("./assets/MapButtons/12(A).png")
map12_s = pygame.image.load("./assets/MapButtons/12(B).png")
map13_d = pygame.image.load("./assets/MapButtons/13(A).png")
map13_s = pygame.image.load("./assets/MapButtons/13(B).png")
map14_d = pygame.image.load("./assets/MapButtons/14(A).png")
map14_s = pygame.image.load("./assets/MapButtons/14(B).png")

map_button_default_imgs = [map1_d, map2_d, map3_d, map4_d, map5_d, map6_d, map7_d, map8_d, map9_d, map10_d, map11_d, map12_d, map13_d, map14_d]
map_button_selected_imgs = [map1_s, map2_s, map3_s, map4_s, map5_s, map6_s, map7_s, map8_s, map9_s, map10_s, map11_s, map12_s, map13_s, map14_s]

# Load alg buttons images
bfs_default = pygame.image.load("./assets/AlgorithmButtons/BFS(A).png")
bfs_selected = pygame.image.load("./assets/AlgorithmButtons/BFS(B).png")
dfs_default = pygame.image.load("./assets/AlgorithmButtons/DFS(A).png")
dfs_selected = pygame.image.load("./assets/AlgorithmButtons/DFS(B).png")
ucs_default = pygame.image.load("./assets/AlgorithmButtons/UCS(A).png")
ucs_selected = pygame.image.load("./assets/AlgorithmButtons/UCS(B).png")
a_default = pygame.image.load("./assets/AlgorithmButtons/A(A).png")
a_selected = pygame.image.load("./assets/AlgorithmButtons/A(B).png")

alg_button_default_imgs = [bfs_default, dfs_default, ucs_default, a_default]
alg_button_selected_imgs = [bfs_selected, dfs_selected, ucs_selected, a_selected]

# step_count_img = pygame.image.load("./assets/MapButtons/StepCount.png")

# Create button
scale_button = 0.15
play_button = Button(x_pos_board + w_board//2 - play_btn_img.get_width()*scale_button - 25, w_board + 10, play_btn_img, scale_button)
reset_button = Button(x_pos_board + w_board//2 + reset_btn_img.get_width()*scale_button + 25, w_board + 10, reset_btn_img, scale_button)
pause_button = Button(x_pos_board + w_board//2 - pause_btn_img.get_width()*scale_button - 25, w_board + 10, pause_btn_img, scale_button)


# Create background map and algorithm buttons
scale_bg_alg = 0.45
background_map = Button(50, 20, background_map_img, 0.4)
background_alg = Button(background_map.rect.x + background_map.rect.width//2 - background_alg_img.get_width()//2*scale_bg_alg, background_map.rect.y + background_map.rect.height + 20, background_alg_img, scale_bg_alg)
# step_count = Button(100, 100, step_count_img, 1)

# screen = pygame.display.set_mode((w, h))
# pygame.display.set_caption("Rush Hour Game")

# Size and position for the node of map
map_button_size = 50
map_button_margin = 18
map_grid_cols = 4
map_grid_rows = (len(map_button_default_imgs) + map_grid_cols - 1) // map_grid_cols
selected_map_idx = 0

# Color
white = (255, 255, 255)

def draw_map_buttons(screen, x, y, selected_idx):
    for i, img in enumerate(map_button_default_imgs):
        row = i // map_grid_cols
        col = i % map_grid_cols
        btn_x = x + col * (map_button_size + map_button_margin)
        btn_y = y + row * (map_button_size + map_button_margin)
        if i < len(map_button_selected_imgs) and i == selected_idx:
            btn_img = pygame.transform.scale(map_button_selected_imgs[i], (map_button_size, map_button_size))
        else:
            btn_img = pygame.transform.scale(img, (map_button_size, map_button_size))
        screen.blit(btn_img, (btn_x, btn_y))
    return

def get_map_button_at_pos(mx, my, x, y):
    for i in range(len(map_button_default_imgs)):
        row = i // map_grid_cols
        col = i % map_grid_cols
        btn_x = x + col * (map_button_size + map_button_margin)
        btn_y = y + row * (map_button_size + map_button_margin)
        rect = pygame.Rect(btn_x, btn_y, map_button_size, map_button_size)
        if rect.collidepoint(mx, my):
            return i
    return None

# Size and position for the node of algorithm
alg_button_size = 70
alg_button_margin = 18
alg_grid_cols = 2
alg_grid_rows = (len(alg_button_default_imgs) + alg_grid_cols - 1) // alg_grid_cols
selected_alg_idx = 0

def draw_alg_buttons(screen, x, y, selected_idx):
    for i, img in enumerate(alg_button_default_imgs):
        row = i // alg_grid_cols
        col = i % alg_grid_cols
        btn_x = x + col * (alg_button_size + alg_button_margin)
        btn_y = y + row * (alg_button_size + alg_button_margin)
        if i < len(alg_button_selected_imgs) and i == selected_idx:
            btn_img = pygame.transform.scale(alg_button_selected_imgs[i], (alg_button_size, alg_button_size))
        else:
            btn_img = pygame.transform.scale(img, (alg_button_size, alg_button_size))
        screen.blit(btn_img, (btn_x, btn_y))
    return

def get_alg_button_at_pos(mx, my, x, y):
    for i in range(len(alg_button_default_imgs)):
        row = i // alg_grid_cols
        col = i % alg_grid_cols
        btn_x = x + col * (alg_button_size + alg_button_margin)
        btn_y = y + row * (alg_button_size + alg_button_margin)
        rect = pygame.Rect(btn_x, btn_y, alg_button_size, alg_button_size)
        if rect.collidepoint(mx, my):
            return i
    return None

def display_console(solution):
    # background_board_orig = pygame.image.load("./assets/background_board.png")
    # background_board_orig = pygame.transform.scale(background_board_orig, (w_board, w_board))
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Rush Hour Game")
    running = True
    is_playing = False
    is_reset = False
    delay_time = 200
    global selected_map_idx
    global selected_alg_idx

    # Position draw grid map buttons on background_map
    map_grid_x = background_map.rect.x + 30
    map_grid_y = background_map.rect.y + 70

    # Position draw grid alg buttons on background_alg
    alg_grid_x = background_alg.rect.x + 40
    alg_grid_y = background_alg.rect.y + 70

    path = solution.path()
    path_len = solution.get_depth()
    node_index = 0
    while running:
        screen.fill((255,255,255))
        map = Board()
        map.readMap(selected_map_idx)
        map.stagePrepare()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                idx_map = get_map_button_at_pos(mx, my, map_grid_x, map_grid_y)
                idx_alg = get_alg_button_at_pos(mx, my, alg_grid_x, alg_grid_y)
                if idx_alg is not None:
                    selected_alg_idx = idx_alg
                if idx_map is not None:
                    selected_map_idx = idx_map
                # Toggle play/pause button
                if (is_playing and pause_button.rect.collidepoint(mx, my)) or (not is_playing and play_button.rect.collidepoint(mx, my)):
                    is_playing = not is_playing
                if (is_reset and reset_button.rect.collidepoint(mx, my)) or (not is_reset and reset_button.rect.collidepoint(mx, my)):
                    is_reset = True
                    node_index = 0
                    is_playing = False
        draw_board(screen, map)

        if is_playing:
            if node_index < path_len:
                pause_button.draw(screen)
                draw_board(screen, path[node_index].state)
                node_index += 1
            else:
                is_playing = False
                draw_board(screen, path[-1].state)
                play_button.draw(screen)
        else:
            play_button.draw(screen)
            if node_index < path_len:
                draw_board(screen, path[node_index].state)
            else:
                draw_board(screen, path[-1].state)
        
        reset_button.draw(screen)
        background_map.draw(screen)
        background_alg.draw(screen)
        # step_count.draw(screen)

        # Draw map button on background_map
        draw_map_buttons(screen, map_grid_x, map_grid_y, selected_map_idx)
        draw_alg_buttons(screen, alg_grid_x, alg_grid_y, selected_alg_idx)
        
        pygame.time.delay(delay_time)
        pygame.display.update()
    pygame.quit()
    exit()

def draw_board(screen, board):
    background_board= pygame.image.load("./assets/background_board.png")
    background_board = pygame.transform.scale(background_board, (w_board, w_board))
    
    for v in board.vehicles:
        curr_v = board.vehicles[v]
        scaled_img = pygame.transform.scale(curr_v.image, (int(curr_v.image.get_width() * scale_board * 0.01), int(curr_v.image.get_height() * scale_board * 0.01)))
        background_board.blit(scaled_img, (curr_v.pos[0] * stride_x + scale_board, curr_v.pos[1] * stride_y + scale_board))
    
    screen.blit(background_board, (x_pos_board, 0))

def display_algo(board):
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Rush Hour Game")
    running = True
    while(running):
        draw_board(screen, board)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        pygame.display.update()

    
    pygame.quit()
    exit()


def draw_step(screen, step_index):
    font = pygame.font.Font(None, 36)
    step_draw = font.render("Step: " + str(step_index), True, (0, 0, 0))
    x_step = 500
    y_step = 620
    screen.blit(step_draw, (x_step, y_step))

def draw_loading(screen):
    screen.fill(white)
    font = pygame.font.Font(None, 48)
    loading_text = font.render("Loading...", True, (0, 0, 0))
    screen.blit(loading_text, (w//2 - 100, h//2 - 50))

def draw_no_solution(screen):
    font = pygame.font.Font(None, 48)
    loading_text = font.render("No solution!", True, (255, 0, 0))
    screen.blit(loading_text, (w//2 - 100, h//2 - 50))