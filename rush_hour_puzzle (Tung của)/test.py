import tkinter as tk
from tkinter import filedialog, ttk

def load_map():
    file_path = filedialog.askopenfilename(filetypes=[("map", "*.txt")])
    if file_path:
        with open(file_path, 'r') as f:
            content = f.read()
            map_display.delete("1.0", tk.END)
            map_display.insert(tk.END, content)
        selected_file.set(file_path)

def run_algorithm():
    algo = algo_choice.get()
    map_data = map_display.get("1.0", tk.END).strip()
    if not map_data:
        result_label.config(text="Vui lòng chọn map.")
        return
    # Thực hiện thuật toán ở đây. Dưới đây chỉ là ví dụ
    result_label.config(text=f"Thuật toán {algo} đang chạy...")

# UI setup
root = tk.Tk()
root.title("Rush Hour Solver")
root.geometry("500x400")

# Drop-down chọn thuật toán
tk.Label(root, text="Chọn thuật toán:").pack()
algo_choice = ttk.Combobox(root, values=["BFS", "DFS", "A*"])
algo_choice.current(0)
algo_choice.pack()

# Nút chọn file map
tk.Button(root, text="Chọn file map", command=load_map).pack(pady=5)

# Hiển thị nội dung map
tk.Label(root, text="Nội dung map:").pack()
map_display = tk.Text(root, height=10, width=50)
map_display.pack()

# Nút chạy
tk.Button(root, text="Chạy thuật toán", command=run_algorithm).pack(pady=10)

# Kết quả
result_label = tk.Label(root, text="")
result_label.pack()

# Biến lưu file đang chọn
selected_file = tk.StringVar()

root.mainloop()
