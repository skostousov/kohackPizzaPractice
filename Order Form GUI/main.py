import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Pizza Order Forms")
back = "black"
root.configure(bg=back)


class LabelInput(tk.Frame):
    def __init__(
        self, parent, label, inp_cls, inp_args, *args, **kwargs
    ):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text=label, anchor="w")
        self.input = inp_cls(self, **inp_args)
        self.columnconfigure(1, weight=1)
        self.label.grid(sticky=tk.E + tk.W)
        self.input.grid(row=0, column=1, sticky=tk.E + tk.W)

variables = {}
labels = {"Name":"", "Address":"", "Phone":"", "Topping":"", "Slices":"", "Tracking Number":""}
for i in labels.keys():
    variables[i] = tk.StringVar()
    if i=="Slices":
        labels[i] = LabelInput(root, (i + ": "), tk.Spinbox, {"textvariable":variables[i], "from_":1, "to":8, "increment":1}, bg=back)
        labels[i].input.configure(borderwidth=2, relief="solid", highlightthickness = 4, highlightcolor="red")
    elif i=="Topping":
        labels[i] = LabelInput(root, (i + ": "), ttk.Combobox, {"textvariable":variables[i], "value":["Cheese"]}, bg=back)
    else:
        labels[i] = LabelInput(root, (i + ": "), tk.Entry, {"textvariable":variables[i]}, bg=back)
        labels[i].input.configure(borderwidth=2, relief="solid", highlightthickness = 4, highlightcolor="red")
    labels[i].label.configure(bg="black", foreground="white", font=("Arial",12, "bold"))
    labels[i].grid(column=1, sticky=tk.E+tk.W, padx=10, pady=2)
def orderinfo():
    orderinfo = {"Name":labels["Name"].input.get(), "Address":labels["Address"].input.get(), "Phone":labels["Phone"].input.get(), "Topping":labels["Topping"].input.get(), "Slices":labels["Slices"].input.get(), "Tracking Number":labels["Tracking Number"].input.get()}
    confirm = messagebox.askokcancel("Confirm Order", "Are you sure you want to confirm order?")
    if confirm==True:    
        print(orderinfo)
        return orderinfo
pizzahut = tk.PhotoImage(file='pizza(2)(1).png')
label = tk.Label(root, text="PizzaHut", image=pizzahut)
label.grid(sticky=tk.W + tk.E, column=1)

Order = tk.Button(root, text="Proceed", command=lambda: orderinfo(), background="white", foreground="black", font=("Arial",14, "bold"), borderwidth=10, relief="solid", highlightthickness = 4, highlightcolor="red").grid(column = 1, sticky = tk.W + tk.E)




root.mainloop()
