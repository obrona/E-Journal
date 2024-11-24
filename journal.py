import tkinter as tk
from tkinter import ttk













class Page1:
    def __init__(self):
        self.page1 = tk.Tk()
        self.page1.title('Page 1')
        self.page1.geometry('1200x900')
        label1_1 = ttk.Label(master=self.page1, text='Self Discovery and Growth', font='Calibri 20')
        label1_2 = ttk.Label(master=self.page1, text='Daily Journal', font ='Calibri 20')
        label1_1.pack(pady=100)
        label1_2.pack(pady=100)
        
        def button_press():
            pg2 = Page2()
        button1_1 = ttk.Button(master=self.page1, text='Next page', command=button_press)
        button1_1.pack()

    def run(self):
        self.page1.mainloop()



class Page2:
    def __init__(self):
        self.page2 = tk.Toplevel()
        self.page2.title('Page 2')
        self.page2.geometry('1200x900')
        label2_1 = ttk.Label(master=self.page2, text='This journal belongs to', font='Calibri 20')
        label2_1.pack()
        entry2_1_var = tk.StringVar()
        entry2_1 = ttk.Entry(master=self.page2, textvariable=entry2_1_var)
        entry2_1.pack()


pg = Page1()
pg.run()