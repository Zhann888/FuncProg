# 13. Сделать индикатор прогресса, который реактивно обновляется в процессе загрузки файла

import tkinter as tk
from tkinter import filedialog
import time
import threading


def load_file():
    for i in range(1, 6):
        time.sleep(1)
        progress = i * 20
        print(f"Прогресс загрузки файла: {progress}%")
        progress_label.config(text=f"Прогресс загрузки файла: {progress}%")
        root.update()
    root.after(1000, message)


def message():
    print("Файл успешно загружен:", selected_file)
    progress_label.config(text="Файл успешно загружен: " + selected_file)


def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    if selected_file:
        print("Загрузка файла:", selected_file)
        threading.Thread(target=load_file).start()

root = tk.Tk()

load_button = tk.Button(root, text="Загрузить файл", command=select_file)
load_button.pack(pady=20)

progress_label = tk.Label(root, text="")
progress_label.pack()

root.mainloop()
