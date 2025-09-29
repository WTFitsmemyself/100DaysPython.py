import tkinter as tk

window = tk.Tk()
window.title("First GUI Program")
window.minsize(500, 400)
window.config(padx=300, pady=400)


#Label
my_label = tk.Label(window, text="NATO", font=("Arial", 20, "bold"), padx=20, pady=20)
my_label.grid(column=0, row=0)

my_label['text'] = "NATO"
my_label.config(text="New Text")


#button

def button_clicked():
    my_label['text'] = input.get()

button = tk.Button(window, text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


button_new = tk.Button(window, text="Click Me", command=button_clicked)
button_new.grid(column=2, row=0)


#input
input = tk.Entry()
input.grid(column=3, row=2)
input.get()



window.mainloop()