import tkinter as tk
from tkinter import ttk, messagebox
from file_selector import FileSelector
from decklist_generator import generate_decklist
from utils import shorten_path
from typing import Optional
import sys

class App(tk.Tk):
    def __init__(self, input_file:Optional[str]=None, output_file:Optional[str]=None):
        super().__init__()
        self.geometry("600x250")
        self.title("Decklist Generator")

        self.input_file = tk.StringVar(value=input_file)
        self.output_file = tk.StringVar(value=output_file)
        self.date = tk.StringVar()
        self.event = tk.StringVar()
        self.location = tk.StringVar()
        self.deck_name = tk.StringVar()
        self.deck_designer = tk.StringVar()
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # input file
        input_label = ttk.Label(self, text="Input File")
        input_label.grid(row=0, column=0)
        input_selector = FileSelector(self, mode="open", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], label_width=100, file_var=self.input_file)
        input_selector.grid(row=0, column=1, sticky="ew")

        # output file
        output_label = ttk.Label(self, text="Output File")
        output_label.grid(row=1, column=0)
        output_selector = FileSelector(self, mode="save", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")], label_width=100, file_var=self.output_file)
        output_selector.grid(row=1, column=1, sticky="ew")

        # date
        date_label = ttk.Label(self, text="Date")
        date_label.grid(row=3, column=0)
        date_entry = ttk.Entry(self, textvariable=self.date)
        date_entry.grid(row=3, column=1, sticky="ew")

        # event
        event_label = ttk.Label(self, text="Event")
        event_label.grid(row=4, column=0)
        event_entry = ttk.Entry(self, textvariable=self.event)
        event_entry.grid(row=4, column=1, sticky="ew")

        # location
        location_label = ttk.Label(self, text="Location")
        location_label.grid(row=5, column=0)
        location_entry = ttk.Entry(self, textvariable=self.location)
        location_entry.grid(row=5, column=1, sticky="ew")

        # deck name
        deck_name_label = ttk.Label(self, text="Deck Name")
        deck_name_label.grid(row=6, column=0)
        deck_name_entry = ttk.Entry(self, textvariable=self.deck_name)
        deck_name_entry.grid(row=6, column=1, sticky="ew")

        # deck designer
        deck_designer_label = ttk.Label(self, text="Deck Designer")
        deck_designer_label.grid(row=7, column=0)
        deck_designer_entry = ttk.Entry(self, textvariable=self.deck_designer)
        deck_designer_entry.grid(row=7, column=1, sticky="ew")

        # first name
        first_name_label = ttk.Label(self, text="First Name")
        first_name_label.grid(row=8, column=0)
        first_name_entry = ttk.Entry(self, textvariable=self.first_name)
        first_name_entry.grid(row=8, column=1, sticky="ew")

        # last name
        last_name_label = ttk.Label(self, text="Last Name")
        last_name_label.grid(row=9, column=0)
        last_name_entry = ttk.Entry(self, textvariable=self.last_name)
        last_name_entry.grid(row=9, column=1, sticky="ew")

        # generate button
        generate_button = ttk.Button(self, text="Generate Decklist", command=self.generate_decklist)
        generate_button.grid(row=10, column=0, columnspan=2)

        self.grid_columnconfigure(1, weight=1)


    def generate_decklist(self):
        input_file = self.input_file.get()
        output_file = self.output_file.get()
        if not (input_file and output_file):
            messagebox.showwarning("Warning", "Please select an input and output file.")
            return
        generate_decklist(
            input_file,
            output_file,
            self.date.get(),
            self.event.get(),
            self.location.get(),
            self.deck_name.get(),
            self.deck_designer.get(),
            self.first_name.get(),
            self.last_name.get()
        )
        messagebox.showinfo("Success", f"Decklist generated: {output_file}")


if __name__ == "__main__":
    app = App(*sys.argv[1:])
    app.mainloop()