#Package
from tkinter import *

#Window setting
window = Tk()
window.config(pady=20, padx=20)
window.title('Mile to Km Convertor')


#input
input = Entry(width=10)
input.grid(column=1, row=0)


#Labels
label = Label(text="Miles")
label.grid(column=2, row=0)


#Label2
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)


#Label3
label3 = Label(text="0")
label3.grid(column=1, row=1)


#Label4
label4 = Label(text="Km")
label4.grid(column=2, row=1)

#function
def miles_to_km():
    miles = float(input.get())
    km = miles * 1.60934
    label3.config(text=str(km))

#calls action() when pressed
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()