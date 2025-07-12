from ui import *
from algorithms import Problem, Node, depth_first_tree_search, breadth_first_tree_search, ucs_search, a_star_search

def solve_by_search(idx_algo, problem):
    if idx_algo == 0:
        return breadth_first_tree_search(problem)
    elif idx_algo == 1:
        return depth_first_tree_search(problem)
    elif idx_algo == 2:
        return ucs_search(problem)
    elif idx_algo == 3:
        return a_star_search(problem)
    else:
        raise Exception("Algorithm is not valid")

def initial_map(selected_map_idx):
    map = Board()
    map.readMap(selected_map_idx)
    map.stagePrepare()
    return map

def solve():
    pygame.init()
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



    selected_map_idx = idx_map_arg = 0
    selected_alg_idx = idx_alg_arg = 0
    path = []
    path_len = 0
    initial_state = initial_map(selected_map_idx)
    is_algo_changed = True
    is_map_changed = True
    node_index = 0
    while running:

        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                idx_map_arg = get_map_button_at_pos(mx, my, map_grid_x, map_grid_y)
                idx_alg_arg = get_alg_button_at_pos(mx, my, alg_grid_x, alg_grid_y)
                
                #Initial state + map + button
                if selected_map_idx != idx_map_arg and idx_map_arg != None:
                    print(idx_map_arg)
                    selected_map_idx = idx_map_arg
                    
                    node_index = 0
                    initial_state = initial_map(selected_map_idx)
                    is_map_changed = True
                    is_playing = False
                    path = []
                    path_len = 0

                if selected_alg_idx != idx_alg_arg and idx_alg_arg != None:
                    node_index = 0
                    selected_alg_idx = idx_alg_arg
                    is_algo_changed = True
                    path = []
                    path_len = 0
                
                if (is_map_changed == True or is_algo_changed == True) and play_button.rect.collidepoint(mx, my) and not is_playing:
                    print("Loading algorithm...")
                    problem = Problem(initial_state, None)
                    solution = solve_by_search(selected_alg_idx, problem)
                    path = solution.path()
                    path_len = solution.get_depth()

                    is_map_changed = is_algo_changed = False                    

                # Toggle play/pause button

                
                if (is_playing and pause_button.rect.collidepoint(mx, my)) or (not is_playing and play_button.rect.collidepoint(mx, my)):
                    is_playing = not is_playing
                if (is_reset and reset_button.rect.collidepoint(mx, my)) or (not is_reset and reset_button.rect.collidepoint(mx, my)):
                    is_reset = True
                    node_index = 0
                    is_playing = False
        # draw_board(screen, map)

        if is_playing:
            if node_index == 0:
                draw_board(screen, initial_state)
                pause_button.draw(screen)
                node_index += 1
            elif node_index < path_len:
                pause_button.draw(screen)
                draw_board(screen, path[node_index].state)
                node_index += 1
            else:
                is_playing = False
                draw_board(screen, path[-1].state)
                play_button.draw(screen)
        else:
            play_button.draw(screen)
            if node_index == 0:
                draw_board(screen, initial_state)
            elif 0 < node_index < path_len:
                draw_board(screen, path[node_index].state)
            else:
                draw_board(screen, path[-1].state)
        
        reset_button.draw(screen)
        background_map.draw(screen)
        background_alg.draw(screen)
        # step_count.draw(screen)

        # Draw map button on background_map
        draw_step(screen, node_index)
        draw_map_buttons(screen, map_grid_x, map_grid_y, selected_map_idx)
        draw_alg_buttons(screen, alg_grid_x, alg_grid_y, selected_alg_idx)
        
        pygame.time.delay(delay_time)
        pygame.display.update()
    pygame.quit()
    exit()