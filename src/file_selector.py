import tkinter as tk
from tkinter import ttk, filedialog
import os
from utils import shorten_path

class FileSelector(ttk.Frame):
    def __init__(self, parent, mode="open", defaultextension=None, filetypes=[("All Files", "*.*")], label_width="", button_width="", file_var=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.mode = mode
        self.defaultextension = defaultextension
        self.filetypes = filetypes
        self.file_var = file_var or tk.StringVar()
        self.short_file_var = tk.StringVar()
        self.set_short_file_path()

        # Label showing selected file
        file_label = ttk.Label(self, textvariable=self.short_file_var, width=label_width)
        file_label.grid(row=0, column=0, columnspan=2, sticky="w")

        # "Browse" button
        browse_btn = ttk.Button(self, text="Browse", command=self.browse_file, width=button_width)
        browse_btn.grid(row=0, column=1, sticky="e")

        self.grid_columnconfigure(1, weight=1)

    def browse_file(self):
        """Open a file dialog and set the selected file path."""
        if self.mode == "open":
            file_path = filedialog.askopenfilename(
                defaultextension=self.defaultextension,
                filetypes=self.filetypes,
                title="Select a file"
            )
        elif self.mode == "save":
            file_path = filedialog.asksaveasfilename(
                defaultextension=self.defaultextension,
                filetypes=self.filetypes,
                title="Select a file"
            )
        else:
            raise ValueError(f"Invalid mode: {self.mode}")
        if file_path:
            self.file_var.set(file_path)
            self.set_short_file_path()

    def set_short_file_path(self):
        self.short_file_var.set(shorten_path(self.file_var.get()))