import tkinter as tk
from tkinter import filedialog

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding as 'utf-8'
            content = file.readlines()
            num_rows = len(content)
            num_cols = max(len(line.strip()) for line in content)
            words = sum(len(line.split()) for line in content)
            letter_count = sum(len(word) for line in content for word in line.split())

            rows_label.config(text=f"Number of Rows: {num_rows}")
            cols_label.config(text=f"Number of Columns: {num_cols}")
            words_label.config(text=f"Number of Words: {words}")
            letter_count_label.config(text=f"Total Letter Count: {letter_count}")


root = tk.Tk()
root.title("Text File Analyzer")
root.geometry("500x400")  # Set window size to 500x400 pixels

main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

browse_button = tk.Button(main_frame, text="Browse", command=load_file)
browse_button.grid(row=0, column=0, pady=5)

rows_label = tk.Label(main_frame, text="Number of Rows: -")
rows_label.grid(row=1, column=0, sticky='w', pady=2)

cols_label = tk.Label(main_frame, text="Number of Columns: -")
cols_label.grid(row=2, column=0, sticky='w', pady=2)

words_label = tk.Label(main_frame, text="Number of Words: -")
words_label.grid(row=3, column=0, sticky='w', pady=2)

letter_count_label = tk.Label(main_frame, text="Total Letter Count: -")
letter_count_label.grid(row=4, column=0, sticky='w', pady=2)

loading_bar = tk.Label(root, text="Loading Bar Placeholder")
loading_bar.pack(side='bottom', fill='x')

root.mainloop()
