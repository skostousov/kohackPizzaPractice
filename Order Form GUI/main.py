import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Pizza Order Form")


class InputLabel(tk.Frame):
    def __init__(self, parent, label, inp_cls, inp_args, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, parent, text=label, anchor='w')
        self.input = inp_cls(self, **inp_args)
        self.columnconfigure(1, weight = 1)
        self.label.grid(sticky = tk.E + tk.W)
        self.input.grid(row=0, column = 1, sticky = tk.E +tk.W)

variables = {}
labels = ["name", "email", "address", "phone", "topping", "slices", "tracking number"]
for i in labels:
    variables[i] = tk.StringVar()
    labels[i] = InputLabel(root, (i + ": "), tk.Entry, {"textvariable":variables[i]})
    labels[i].grid()

root.mainloop()

