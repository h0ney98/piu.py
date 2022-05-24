import tkinter as tk  # as переименовывет ткинтер в ТК
from tkinter import *
import webbrowser

JPEGER = tk.Tk()
JPEGER.title(' JPEGER')
JPEGER.configure(background='#555')
JPEGER.geometry('600x700+200+100')



def search():
    webbrowser.open('https://vk.com/away.php?to=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FSpecial%3ARandom%2FFile&el=snippet')


btn1 = Button(text="TOUCH ME ", background="#555", foreground="#ccc",command=search,padx="15", pady="6", font="15")
btn1.pack(side=BOTTOM)


JPEGER.mainloop()
