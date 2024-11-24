import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

check_var = tk.IntVar()
check = ttk.Checkbutton(master=window, 
                        text='check box 1', 
                        variable=check_var, 
                        command=lambda: print(check_var.get()),
                        onvalue=10,
                        offvalue=5)
check.pack()


window.mainloop()