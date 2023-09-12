
#  Text Editor Using Python.

import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.text = tk.Text(root, wrap=tk.WORD, undo=True, autoseparators=True)
        self.text.pack(expand="yes", fill="both")

        # Initialize variables
        self.dark_mode = False
        self.current_text_color = "black"

        # Create the menu
        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        # File menu
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text.edit_redo)

        # View menu
        self.view_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Toggle Dark/White Mode", command=self.toggle_dark_mode)
        self.view_menu.add_command(label="Change Text Color", command=self.change_text_color)

    def new_file(self):
        self.text.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text.get("1.0", tk.END)
                file.write(content)

    def toggle_dark_mode(self):
        if self.dark_mode:
            self.text.config(bg="white", fg="black")
        else:
            self.text.config(bg="black", fg="white")
        self.dark_mode = not self.dark_mode

    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text.config(fg=color)
            self.current_text_color = color

if __name__ == "__main__":
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()
