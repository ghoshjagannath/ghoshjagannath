# in this python programe only a widget will  be created and we take user argument for 
#current place temparature in  specific

from tkinter import *
from PIL import ImageTk, Image
from weather import temperature_of_place_c,temperature_of_place_f
import tkinter as tk


#root window for main  function.
window=Tk()


#here only windows configuration happend .
# window['bg']='#b7d7e8'

window.title('Weather helper')
window.geometry("400x360+200+200")
window.resizable(False,False)
window.iconbitmap("C:/Users/ghosh/AppData/Local/Programs/Python/Python39/Weather_project/icon.ico")




# add widgets here
#adding icon image of tkinter 
bg = ImageTk.PhotoImage(file ="C:/Users/ghosh/AppData/Local/Programs/Python/Python39/Weather_project/background_photo.jpg")
# Show image using label
label1 = Label( window, image = bg)
label1.place(x =0,y=0)



#adding function for taking city name for weather purpose.
def new_func():
    temperature_of_place_c(textExample.get("1.0","end"))

def new_func2():
    temperature_of_place_f(textExample.get("1.0","end"))



#Text field for taking value of user desire. 
textExample=tk.Text(window, height=10)
textExample.pack()


def viewSelected():
    choice  = var.get()
    if choice == 1:
       new_func()

    elif choice == 2:
        new_func2()

    else:
        print("Invalid selection")


#A tkinter button for initialize for temparature calculation . 
btnRead=tk.Button(window, height=1, width=10, text="Read",command=viewSelected)
btnRead.pack()



var = IntVar()
Radiobutton(window, text="Celcius", variable=var, value=1,).pack()
Radiobutton(window, text="Ferenheit", variable=var, value=2).pack()



window.mainloop()