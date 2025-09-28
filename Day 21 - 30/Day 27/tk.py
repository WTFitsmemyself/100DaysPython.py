import tkinter as tk

window = tk.Tk()
window.title("First GUI Program")
window.minsize(500, 400)


#Label
my_label = tk.Label(window, text="NATO", font=("Arial", 20, "bold"))
my_label.pack()



my_label['text'] = "NATO"
my_label.config(text="New Text")


#button

def button_clicked():
    my_label['text'] = input.get()

button = tk.Button(window, text="Click Me", command=button_clicked)
button.pack()



#input
input = tk.Entry()
input.pack()
input.get()



window.mainloop()