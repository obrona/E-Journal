import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Changeable Pages')
#win.geometry('800x600')


page1 = ttk.Frame(win)
page1.grid(row=0, column=0, sticky='news')
lb1 = ttk.Label(page1, text='I am page 1')
lb1.pack(side='left', anchor='s')
page2 = ttk.Frame(win)
page2.grid(row=0, column=0, sticky='news')
lb2 = ttk.Label(page2, text='I am page 2')
lb2.pack(side='left', anchor='s')


btn1 = ttk.Button(page1, text='go to page 2', command=lambda: page2.tkraise())
btn1.pack(side='right', anchor='s')
btn2 = ttk.Button(page2, text='go to page1', command=lambda: page1.tkraise())
btn2.pack(side='right', anchor='s')





page1.tkraise()
win.geometry('800x600')
win.rowconfigure(0, weight=800)
win.columnconfigure(0, weight=600)
win.mainloop()

