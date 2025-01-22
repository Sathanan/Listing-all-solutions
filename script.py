import os
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font
import subprocess

SEARCH_DIRECTORY = r"C:\Users\sjeyakumar\Desktop\Mini_Projekte"  

def find_sln_files(directory):
    """Find all .sln files in the given directory and its subdirectories."""
    sln_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".sln"):
                sln_files.append(os.path.join(root, file))
    return sln_files

def open_sln_file(file_path):
    """Open the selected .sln file and close the UI."""
    try:
        os.startfile(file_path)  
        window.quit() 
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file: {e}")

def select_and_open_sln():
    """Open a GUI to display .sln files and let the user select one to open."""
    sln_files = find_sln_files(SEARCH_DIRECTORY)
    if not sln_files:
        messagebox.showinfo("No Files", "No .sln files found in the specified directory.")
        return

    global window
    window = tk.Tk()
    window.title("Select your Solution")
    window.geometry("600x400")
    window.config(bg="#f0f0f0")
    window.resizable(False, False) 

    custom_font = font.Font(family="Helvetica", size=12)

    tree = ttk.Treeview(window, columns=("File"), show="headings", height=15)
    tree.heading("File", text="Solution Files")
    tree.column("File", stretch=tk.YES, width=250)
    tree.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    for file in sln_files:
        file_name = os.path.basename(file)  
        tree.insert("", "end", values=(file_name,))

    def on_item_double_click(event):
        selected_item = tree.selection()
        if selected_item:
            file_name = tree.item(selected_item[0], "values")[0]
            file_path = next(file for file in sln_files if os.path.basename(file) == file_name)
            open_sln_file(file_path)

    tree.bind("<Double-1>", on_item_double_click)

    open_button = tk.Button(window, text="Open Selected File", command=on_item_double_click, **{'bg': "#4CAF50", 'fg': "white", 'font': custom_font, 'relief': "flat", 'width': 20})
    open_button.pack(pady=20)

    close_button = tk.Button(window, text="Close", command=window.quit, **{'bg': "#FF6347", 'fg': "white", 'font': custom_font, 'relief': "flat", 'width': 20})
    close_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    select_and_open_sln()
