import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

app = tk.Tk()
app.title(' IMPGPEGER ')
app.configure(background='#ececec')
app.geometry('600x400+200+100')

# #создание текстовой надписи
# app_name = ttk.Label(app, text=' ', font='verdana')
# app_name.grid(row=0, column=2)

#текст
# search_label = ttk.Label(app, text=' Поиск ')
# search_label.grid(row=5, column=3)

#окно ввода
# text_field = ttk.Entry(app, width=50)
# text_field.grid(row=1, column=2)

# search_engine = StringVar()
# search_engine.set('google')


def searchBTM():
    if text_field.get().strip() != "":
        if search_engine.get() == 'google':
            webbrowser.open('https://www.google.ru/?hl=d'+text_field.get())
        elif search_engine.get() == 'yandex':
            webbrowser.open('https://www.google.ru/search?q=' + text_field.get())


def search():
    searchBTM()


btn_search = ttk.Button(app, text='НАЙТИ', width=50, command=search)
btn_search.grid(row=0, column=3)


def enter(event):
    searchBTM()


# переключатели
# radio_google = ttk.Radiobutton(app, text='Google', value='google',variable=search_engine)
# radio_google.grid(row=2,column=2,sticky=W)
#
#
# radio_yandex = ttk.Radiobutton(app, text='Yandex', value='yandex',variable=search_engine)
# radio_yandex.grid(row=2,column=2,sticky=E)




# запуск через событие
# text_field.bind('<Return>', enter)

# #активная строчка поиска
# text_field.focus()


# поверх окон
app.wm_attributes('-topmost', True)

app.mainloop()
