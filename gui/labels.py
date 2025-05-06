import tkinter as tk
from config import label_rust

class LabelCreate:
    def __init__(self, master):
        self.master = master

    def create_label(self, text, cord):
        label = tk.Label(self.master, text=text, font=("Times New Roman", 25))
        label.place(y=cord[0],
                    x=cord[1])