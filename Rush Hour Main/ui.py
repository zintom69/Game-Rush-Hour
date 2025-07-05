import pygame
from puzzle import *
from pygame.locals import *
import os

w = 1000
h = 700

stride_x  = 80
stride_y = 80

# ================== VÙNG VẼ MENU (MAPS, ALGORITHM) ==================
def draw_map_list(screen, maps, selected_map):
    # Vẽ khung menu map với padding trên/dưới, khung ngoài ôm trọn các item
    menu_width = int(w * 4 / 12)
    padding_x = 10
    padding_y = 18
    grid_size = 4  # 4x4
    cell_margin = 8
    cell_size = (menu_width-60 - 2*padding_x - (grid_size+1)*cell_margin) // grid_size
    rect_height = 50 + grid_size*cell_size + (grid_size+1)*cell_margin + padding_y*2
    rect = pygame.Rect(30, 50, menu_width-60, rect_height)
    pygame.draw.rect(screen, (245,245,255), rect, border_radius=15)
    pygame.draw.rect(screen, (100,100,180), rect, 3, border_radius=15)
    font_title = pygame.font.SysFont('arial', 28, bold=True)
    font_cell = pygame.font.SysFont('arial', 22, bold=True)
    # Căn giữa chữ 'Maps'
    text = font_title.render('Maps', True, (60,60,120))
    text_rect = text.get_rect(center=(rect.x+rect.width//2, rect.y+padding_y+18))
    screen.blit(text, text_rect)
    # Vẽ lưới 4x4 số 1-15, ô 16 là ô trống
    start_x = rect.x + padding_x + cell_margin
    start_y = rect.y + padding_y + 40
    num = 1
    for row in range(grid_size):
        for col in range(grid_size):
            # Không vẽ ô cuối cùng (ô trống)
            if row == grid_size-1 and col == grid_size-1:
                continue
            cell_rect = pygame.Rect(
                start_x + col*(cell_size+cell_margin),
                start_y + row*(cell_size+cell_margin),
                cell_size, cell_size
            )
            # Hiệu ứng chọn khi nhấn vào ô
            if selected_map == (row*grid_size+col):
                pygame.draw.rect(screen, (120,180,255), cell_rect, border_radius=8)
                pygame.draw.rect(screen, (60,120,200), cell_rect, 4, border_radius=8)
            else:
                pygame.draw.rect(screen, (230,240,255), cell_rect, border_radius=8)
                pygame.draw.rect(screen, (120,120,180), cell_rect, 2, border_radius=8)
            # Vẽ số 1-15
            t = font_cell.render(str(num), True, (40,40,80))
            text_rect = t.get_rect(center=cell_rect.center)
            screen.blit(t, text_rect)
            num += 1
        else:
            pass  # ô trống không vẽ gì thêm

# Vẽ menu chọn thuật toán bên dưới menu map
# Liên kết: Khi click vào thuật toán sẽ đổi selected_algorithm, dùng để chọn giải thuật cho nút Play

def draw_algorithm_list(screen, algorithms, selected_algorithm):
    # Vẽ khung menu algorithm nhỏ hơn, chỉ bằng 3/4 menu map, layout 2x2 các ô vuông
    menu_width = int(w * 4 / 12)
    alg_width = int((menu_width-60) * 0.75)
    padding_x = 10
    padding_y = 12
    grid_size = 2  # 2x2
    cell_margin = 8
    cell_size = (alg_width - 2*padding_x - (grid_size+1)*cell_margin) // grid_size
    rect_height = 40 + grid_size*cell_size + (grid_size+1)*cell_margin + padding_y*2
    # Tính lại vị trí y dựa trên khung map phía trên
    map_grid_size = 4
    map_cell_margin = 8
    map_cell_size = (menu_width-60 - 2*padding_x - (map_grid_size+1)*map_cell_margin) // map_grid_size
    map_rect_height = 50 + map_grid_size*map_cell_size + (map_grid_size+1)*map_cell_margin + 18*2
    margin_top = 36
    rect_y = 50 + map_rect_height + margin_top
    # Căn giữa theo chiều ngang menu map
    alg_x = 30 + ((menu_width-60) - alg_width)//2
    rect = pygame.Rect(alg_x, rect_y, alg_width, rect_height)
    pygame.draw.rect(screen, (245,245,255), rect, border_radius=15)
    pygame.draw.rect(screen, (100,100,180), rect, 3, border_radius=15)
    font_title = pygame.font.SysFont('arial', 24, bold=True)
    font_cell = pygame.font.SysFont('arial', 18, bold=True)
    # Căn giữa chữ 'Algorithm'
    text = font_title.render('Algorithm', True, (60,60,120))
    text_rect = text.get_rect(center=(rect.x+rect.width//2, rect.y+padding_y+14))
    screen.blit(text, text_rect)
    # Vẽ 2x2 các ô vuông thuật toán
    start_x = rect.x + padding_x + cell_margin
    start_y = rect.y + padding_y + 32
    idx = 0
    for row in range(grid_size):
        for col in range(grid_size):
            if idx >= len(algorithms):
                continue
            cell_rect = pygame.Rect(
                start_x + col*(cell_size+cell_margin),
                start_y + row*(cell_size+cell_margin),
                cell_size, cell_size
            )
            color = (255,220,180) if idx == selected_algorithm else (255,255,255)
            border_col = (180,120,80) if idx == selected_algorithm else (180,120,80)
            pygame.draw.rect(screen, color, cell_rect, border_radius=8)
            pygame.draw.rect(screen, border_col, cell_rect, 2, border_radius=8)
            t = font_cell.render(algorithms[idx], True, (80,60,40))
            text_rect = t.get_rect(center=cell_rect.center)
            screen.blit(t, text_rect)
            idx += 1

# ================== VÙNG VẼ BOARD (VIDEO) ==================
def draw_board(screen, board):
    # Board chiếm toàn bộ vùng content bên phải, sát lề trên, phải, dưới (trừ lề nhỏ)
    content_x = int(w * 4 / 12) + 20
    content_width = w - content_x - 20
    board_height = 420  # Tăng chiều cao cho sát mép dưới vùng content
    board_y = 50
    board_rect = pygame.Rect(content_x, board_y, content_width, board_height)
    pygame.draw.rect(screen, (255,255,255), board_rect, border_radius=18)
    pygame.draw.rect(screen, (80,80,80), board_rect, 4, border_radius=18)
    # Vẽ các xe nếu có board
    if board:
        for v in board.vehicles:
            curr_v = board.vehicles[v]
            screen.blit(curr_v.image, (curr_v.pos[0] * cell_size + board_rect.x  , curr_v.pos[1] * cell_size + board_rect.y))

# ================== VÙNG VẼ STATISTICS (MÔ TẢ/THỐNG KÊ) ==================
def draw_statistics(screen, stats):
    # Statistics sát dưới hai nút, cùng chiều rộng với board
    content_x = int(w * 4 / 12) + 20
    content_width = w - content_x - 20
    board_height = 420
    board_y = 50
    button_y = board_y + board_height + 24
    statistics_height = 90
    statistics_y = button_y + 80
    rect = pygame.Rect(content_x, statistics_y, content_width, statistics_height)
    pygame.draw.rect(screen, (245,245,255), rect, border_radius=16)
    pygame.draw.rect(screen, (100,100,180), rect, 3, border_radius=16)
    font_title = pygame.font.SysFont('arial', 24, bold=True)
    font_item = pygame.font.SysFont('arial', 20)
    # Căn giữa tiêu đề 'Statistics' phía trên các stats
    text = font_title.render('Statistics', True, (60,60,120))
    text_rect = text.get_rect(center=(rect.x+rect.width//2, rect.y+22))
    screen.blit(text, text_rect)
    # Vẽ các thông tin stats, căn giữa ngang
    labels = ['Time', 'Step count', 'Expanded node', 'Memory Usage']
    values = [stats.get(label, '-') for label in labels]
    stat_text = '   |   '.join([f'{label}: {val}' for label, val in zip(labels, values)])
    t = font_item.render(stat_text, True, (40,40,80))
    t_rect = t.get_rect(center=(rect.x+rect.width//2, rect.y+statistics_height//2+18))
    screen.blit(t, t_rect)

# ================== VÙNG VẼ NÚT (PLAY, RESET) ==================
def draw_buttons(screen, is_playing):
    # Hai nút căn giữa theo chiều ngang của board, nằm ngay dưới board, margin rõ ràng
    content_x = int(w * 4 / 12) + 20
    content_width = w - content_x - 20
    board_height = 420
    board_y = 50
    button_y = board_y + board_height + 50  # margin rõ ràng dưới board
    button_radius = 36
    button_gap = 120  # khoảng cách giữa hai nút lớn hơn
    center_x = content_x + content_width // 2
    play_x = center_x - button_radius - button_gap//2
    reset_x = center_x + button_radius + button_gap//2
    import os
    font = pygame.font.SysFont('arial', 18, bold=True)
    # Nút Play/Pause dùng ảnh PNG (hiển thị hình tròn)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    play_img_name = 'pause_btn.png' if is_playing else 'play_btn.png'
    play_img_path = os.path.join(base_dir, 'assets', play_img_name)
    if os.path.exists(play_img_path):
        try:
            play_img = pygame.image.load(play_img_path).convert_alpha()
            play_img = pygame.transform.smoothscale(play_img, (button_radius*2, button_radius*2))
            mask = pygame.Surface((button_radius*2, button_radius*2), pygame.SRCALPHA)
            pygame.draw.circle(mask, (255,255,255,255), (button_radius, button_radius), button_radius)
            play_img.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
            screen.blit(play_img, (play_x-button_radius, button_y-button_radius))
        except Exception as e:
            print(f"[ERROR] Không thể load ảnh nút play/pause: {e}")
            pygame.draw.circle(screen, (60,180,80), (play_x, button_y), button_radius)
            pygame.draw.circle(screen, (255,255,255), (play_x, button_y), button_radius, 4)
    else:
        print(f"[ERROR] Không tìm thấy file ảnh: {play_img_path}")
        pygame.draw.circle(screen, (60,180,80), (play_x, button_y), button_radius)
        pygame.draw.circle(screen, (255,255,255), (play_x, button_y), button_radius, 4)
    # Nút Reset dùng ảnh PNG (hiển thị hình tròn)
    reset_img_path = os.path.join(base_dir, 'assets', 'reset_btn.png')
    if os.path.exists(reset_img_path):
        try:
            reset_img = pygame.image.load(reset_img_path).convert_alpha()
            reset_img = pygame.transform.smoothscale(reset_img, (button_radius*2, button_radius*2))
            # Tạo surface tròn mask
            mask = pygame.Surface((button_radius*2, button_radius*2), pygame.SRCALPHA)
            pygame.draw.circle(mask, (255,255,255,255), (button_radius, button_radius), button_radius)
            # Áp dụng mask alpha lên ảnh
            reset_img.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
            screen.blit(reset_img, (reset_x-button_radius, button_y-button_radius))
        except Exception as e:
            print(f"[ERROR] Không thể load ảnh nút reset: {e}")
            orange = (255,204,102)
            pygame.draw.circle(screen, orange, (reset_x, button_y), button_radius)
            pygame.draw.circle(screen, (255,255,255), (reset_x, button_y), button_radius, 4)
    else:
        print(f"[ERROR] Không tìm thấy file ảnh: {reset_img_path}")
        orange = (255,204,102)
        pygame.draw.circle(screen, orange, (reset_x, button_y), button_radius)
        pygame.draw.circle(screen, (255,255,255), (reset_x, button_y), button_radius, 4)

# ================== XỬ LÝ SỰ KIỆN CHỌN MENU, NÚT ==================
def handle_map_selection(event, maps, selected_map):
    # Xử lý click chọn map, trả về chỉ số map mới (ô nào được chọn thì highlight)
    menu_width = int(w * 4 / 12)
    padding_x = 10
    padding_y = 18
    grid_size = 4
    cell_margin = 8
    cell_size = (menu_width-60 - 2*padding_x - (grid_size+1)*cell_margin) // grid_size
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mx, my = event.pos
        start_x = 30 + padding_x + cell_margin
        start_y = 50 + padding_y + 40
        for row in range(grid_size):
            for col in range(grid_size):
                # Không xử lý ô cuối cùng (ô trống)
                if row == grid_size-1 and col == grid_size-1:
                    continue
                idx = row*grid_size+col
                cell_rect = pygame.Rect(
                    start_x + col*(cell_size+cell_margin),
                    start_y + row*(cell_size+cell_margin),
                    cell_size, cell_size
                )
                if cell_rect.collidepoint(mx, my):
                    return idx
    return selected_map

def handle_algorithm_selection(event, algorithms, selected_algorithm):
    # Xử lý click chọn thuật toán, trả về chỉ số thuật toán mới (layout 2x2, khung nhỏ hơn)
    menu_width = int(w * 4 / 12)
    alg_width = int((menu_width-60) * 0.75)
    padding_x = 10
    padding_y = 12
    grid_size = 2
    cell_margin = 8
    cell_size = (alg_width - 2*padding_x - (grid_size+1)*cell_margin) // grid_size
    map_grid_size = 4
    map_cell_margin = 8
    map_cell_size = (menu_width-60 - 2*padding_x - (map_grid_size+1)*map_cell_margin) // map_grid_size
    map_rect_height = 50 + map_grid_size*map_cell_size + (map_grid_size+1)*map_cell_margin + 18*2
    margin_top = 36
    rect_y = 50 + map_rect_height + margin_top
    alg_x = 30 + ((menu_width-60) - alg_width)//2
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mx, my = event.pos
        idx = 0
        start_x = alg_x + padding_x + cell_margin
        start_y = rect_y + padding_y + 32
        for row in range(grid_size):
            for col in range(grid_size):
                if idx >= len(algorithms):
                    continue
                cell_rect = pygame.Rect(
                    start_x + col*(cell_size+cell_margin),
                    start_y + row*(cell_size+cell_margin),
                    cell_size, cell_size
                )
                if cell_rect.collidepoint(mx, my):
                    return idx
                idx += 1
    return selected_algorithm

def handle_play_pause_button(event, is_playing):
    # Xử lý click nút Play/Pause, trả về trạng thái mới
    content_x = int(w * 4 / 12) + 20
    content_width = w - content_x - 20
    board_height = 420
    board_y = 50
    button_y = board_y + board_height + 50
    button_radius = 36
    button_gap = 120
    center_x = content_x + content_width // 2
    play_x = center_x - button_radius - button_gap//2
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mx, my = event.pos
        if (mx-play_x)**2 + (my-button_y)**2 <= button_radius**2:
            return not is_playing
    return is_playing

def handle_reset_button(event):
    # Xử lý click nút Reset, trả về True nếu click
    # Liên kết: Được gọi trong main_gui, khi True thì reset lại trạng thái board
    reset_x = int(w * 4 / 12) + 200
    reset_y = 520
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mx, my = event.pos
        if (mx-reset_x)**2 + (my-reset_y)**2 <= 36**2:
            return True
    return False

def update_stats(time, step_count, expanded_node, memory_usage):
    # Hàm tạo dict stats để truyền cho draw_stats
    # Liên kết: Được gọi khi cập nhật thông tin thống kê sau khi giải xong
    return {
        'Time': time,
        'Step count': step_count,
        'Expanded node': expanded_node,
        'Memory Usage': memory_usage
    }

def load_board_from_map(map_id):
    # Hàm này cần trả về một instance board tương ứng với map_id
    # Nếu không load được, trả về board giả lập để không bị crash giao diện
    try:
        from puzzle import Board
        return Board(map_id)
    except Exception as e:
        print(f"[ERROR] Không thể load board cho map {map_id}: {e}")
        # Board giả lập cho test giao diện (không có xe)
        class DummyBoard:
            def __init__(self):
                self.vehicles = {}
            def move(self, vid, step):
                pass
        return DummyBoard()

# ================== HÀM MAIN GIAO DIỆN ==================
def main_gui():
    # Hàm khởi tạo và chạy vòng lặp giao diện chính
    # Liên kết: Gọi các hàm vẽ và xử lý sự kiện ở trên
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Rush Hour Game")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((240,240,240))
    
    # Dữ liệu mẫu
    maps = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15']
    algorithms = ['BFS', 'DFS', 'UCS', 'A*']
    selected_map = 0
    selected_algorithm = 0
    stats = update_stats('-', '-', '-', '-')
    # ==== BỔ SUNG: Viết logic load board thực tế ở file khác và import vào đây ====
    board = load_board_from_map(maps[selected_map])  # Mặc định hiển thị map 1
    running = True
    is_playing = False
    last_move_time = pygame.time.get_ticks()
    move_delay = 1000  # ms
    # ==== BỔ SUNG: Viết các hàm giải thuật, trả về step list/generator, import vào ====
    solver_steps = None  # Lưu iterator/generator các bước giải
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            # Xử lý chọn menu và nút
            new_selected_map = handle_map_selection(event, maps, selected_map)
            if new_selected_map != selected_map:
                selected_map = new_selected_map
                # ==== BỔ SUNG: Viết logic load board thực tế ở file khác và import vào đây ====
                new_board = load_board_from_map(maps[selected_map])
                if new_board is not None:
                    board = new_board  # Chỉ cập nhật nếu load thành công
                    is_playing = False  # Dừng auto-play khi đổi map
                    # ==== BỔ SUNG: Khi đổi map, cần reset solver_steps về None ====
                    solver_steps = None
                else:
                    print(f"[ERROR] Không thể load board cho map {maps[selected_map]}, giữ nguyên board cũ!")
            
            # Xử lý chọn thuật toán
            # Nếu thuật toán được chọn khác, reset board và dừng auto-play
            new_selected_algorithm = handle_algorithm_selection(event, algorithms, selected_algorithm)
            if new_selected_algorithm != selected_algorithm:
                selected_algorithm = new_selected_algorithm
                # ==== BỔ SUNG: Khi đổi thuật toán, reset lại board về trạng thái ban đầu ====
                new_board = load_board_from_map(maps[selected_map])
                if new_board is not None:
                    board = new_board
                    is_playing = False
                    # ==== BỔ SUNG: Khi đổi thuật toán, cần reset solver_steps về None ====
                    solver_steps = None
                else:
                    print(f"[ERROR] Không thể reset board khi đổi thuật toán, giữ nguyên board cũ!")
            prev_is_playing = is_playing
            is_playing = handle_play_pause_button(event, is_playing) if board else False
            if is_playing and not prev_is_playing:
                last_move_time = pygame.time.get_ticks()  # Reset timer khi bắt đầu play
                # ==== BỔ SUNG: Khi Play, lấy step list/generator từ thuật toán đã chọn ====
                # solver_steps = solve_board(board, selected_algorithm)  # <-- Viết hàm này ở file khác và import vào
            if handle_reset_button(event):
                new_board = load_board_from_map(maps[selected_map])
                if new_board is not None:
                    board = new_board
                    is_playing = False
                    # ==== BỔ SUNG: Khi reset, cần reset solver_steps về None ====
                    solver_steps = None
                else:
                    print(f"[ERROR] Không thể reset board cho map {maps[selected_map]}, giữ nguyên board cũ!")
        # Auto-play: chỉ chạy khi đang play và có board
        if is_playing and board is not None:
            now = pygame.time.get_ticks()
            if now - last_move_time >= move_delay:
                # ==== BỔ SUNG: Khi Play, lấy step tiếp theo từ thuật toán đã chọn ====
                # Ví dụ:
                # if solver_steps is not None:
                #     try:
                #         move = next(solver_steps)
                #         board.move(*move)
                #     except StopIteration:
                #         is_playing = False  # Dừng khi hết bước
                # else:
                #     pass
                board.move("0", 1)  # Thay bằng logic move thực tế
                last_move_time = now
        screen.blit(background, (0,0))
        draw_map_list(screen, maps, selected_map)
        draw_algorithm_list(screen, algorithms, selected_algorithm)
        if board:
            draw_board(screen, board)
        else:
            draw_board(screen, None)
        draw_buttons(screen, is_playing)
        draw_statistics(screen, stats)
        pygame.display.update()
    pygame.quit()

# ========== END ==========
if __name__ == "__main__":
    main_gui()
