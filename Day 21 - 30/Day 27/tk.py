import tkinter as tk

window = tk.Tk()
window.title("First GUI Program")
window.minsize(500, 400)


#Label
my_label = tk.Label(window, text="NATO", font=("Arial", 20, "bold"))
my_label.pack()



window.mainloop()