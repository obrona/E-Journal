import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Tkinter Variable')
window.geometry('400x300')


string_var = tk.StringVar(value=0)

label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

entry2 = ttk.Entry(master=window, textvariable=string_var)
entry2.pack()

window.mainloop()