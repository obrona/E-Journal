import tkinter as tk
from tkinter import ttk


class Page:
    def __init__(self, what_page, window):
        self.next_page = None
        self.prev_page = None
        self.frame = tk.Frame(window)
        self.frame.grid(row=0, column=0, sticky='news')
        self.modifiable = tk.Frame(self.frame, background='#32a8a4')
        self.modifiable.pack(side='top', expand='true', fill='both')

        self.navigate = tk.Frame(self.frame, width=800, height=50)
        self.navigate.pack(side='bottom')
        self.btn = ttk.Button(self.navigate, text='Next Page')
        self.btn2 = ttk.Button(self.navigate, text='Prev Page')
        self.lb = ttk.Label(self.navigate, text='Page ' + str(what_page))
        self.btn.pack(side='right')
        self.lb.pack(side='right')
        self.btn2.pack(side='right')


        
    
    def set_next_page(self, next_page):
        self.btn.configure(command=lambda: next_page.frame.tkraise())

    def set_prev_page(self, prev_page):
        self.btn2.configure(command=lambda: prev_page.frame.tkraise())

    def make_1st(self):
        self.frame.tkraise()
    
    def get_modifiable_frame(self):
        return self.modifiable
    

class QnA(tk.Frame):
    def __init__(self, parent, question):
        super().__init__(parent)
        self.configure(background='green')
        self.question = ttk.Label(self, text=question, foreground='#faf7f7', background='green', font='Calibri 25')
        self.entry = tk.Text(self, height=3, width=20)
        self.question.pack(side='left')
        self.entry.pack(side='left')

    
    
class GridRadioBtn(tk.Frame):
    def __init__(self, parent, matrix):
        super().__init__(parent)
        self.var = tk.StringVar()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ttk.Radiobutton(self, text=matrix[i][j], variable=self.var, value=matrix[i][j]).grid(row=i, column=j)
      
        
    

    

win = tk.Tk()
win.geometry('800x400')
win.rowconfigure(0, weight=800)
win.columnconfigure(0, weight=600)
lst = []
for i in range(6):
    lst.append(Page(i, win))

for i in range(6):
    nxt = (i + 1) % 6
    prev = i - 1 if (i - 1 >= 0) else 5
    lst[i].set_next_page(lst[nxt])
    lst[i].set_prev_page(lst[prev])


#page1
lb1_1 = ttk.Label(lst[0].get_modifiable_frame(), text='Self Discovery and Growth', foreground='#faf7f7', background='green', font='Calibri 25')
lb1_2 = ttk.Label(lst[0].get_modifiable_frame(), text='Daily Journal',foreground='#faf7f7', background='green', font='Calibri 25')
lb1_1.pack()
lb1_2.pack(pady=20)



#page2
lb2_1 = ttk.Label(lst[1].get_modifiable_frame(), text='This Jounal belongs to', foreground='#faf7f7', background='green', font='Calibri 25')
entry_var2_1 = tk.StringVar()
entry2_1 = ttk.Entry(lst[1].get_modifiable_frame(), textvariable=entry_var2_1, width=20, font=("Arial", 12), justify='center')
lb2_1.pack()
entry2_1.pack(pady=20)

#page3
lb3_1 = ttk.Label(lst[2].get_modifiable_frame(), text='Daily Check In', foreground='#faf7f7', background='green', font='Calibri 25')
lb3_1.pack()
QnA(lst[2].get_modifiable_frame(), 'How are you feeling today?').pack()
QnA(lst[2].get_modifiable_frame(), 'Things you are greatful for').pack()
QnA(lst[2].get_modifiable_frame(), 'Today Affirmation').pack()

matrix = [['calm', 'rested', 'Annoyed'], ['Happy', 'Angry', 'Sad'], ['Anxious', 'Stress', 'Other']]
fr3_1 = tk.Frame(lst[2].get_modifiable_frame(), background='green')
grid = GridRadioBtn(fr3_1, matrix)
lb3_2 = ttk.Label(fr3_1, text='My mood is', foreground='#faf7f7', background='green', font='Calibri 25')
lb3_2.pack(side='left')
grid.pack(side='left')
fr3_1.pack()


#page4
ttk.Label(lst[3].get_modifiable_frame(), text='Something on your mind', foreground='#faf7f7', background='green', font='Calibri 25').pack()
ttk.Label(lst[3].get_modifiable_frame(), text='Reflection and Self Analysis', foreground='#faf7f7', background='green', font='Calibri 25').pack()
ttk.Label(lst[3].get_modifiable_frame(), text='Creative Expression', foreground='#faf7f7', background='green', font='Calibri 25').pack()
ttk.Label(lst[3].get_modifiable_frame(), text='Daily Habits and Self Care', foreground='#faf7f7', background='green', font='Calibri 25').pack()
ttk.Label(lst[3].get_modifiable_frame(), text='Personal Goals', foreground='#faf7f7', background='green', font='Calibri 25').pack()






#page5
canvas = tk.Canvas(lst[4].get_modifiable_frame(), scrollregion=(0, 0, 800, 1200))
scrollable_frame = tk.Frame(canvas, background='#32a8a4')

scrollbar = ttk.Scrollbar(lst[4].get_modifiable_frame(), orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
file = open('advice.txt', 'r')
ttk.Label(scrollable_frame, text='Affirmative Words', foreground='#faf7f7', background='green', font = 'Arial 20').pack()
for i in range(20):
    ttk.Label(scrollable_frame, text=file.readline(), foreground='#faf7f7', background='green').pack(pady=10)

canvas.create_window((0, 0), window=scrollable_frame, anchor='nw', width=800, height=1200)
scrollbar.pack(side='right', fill='y')
canvas.pack(expand=True, fill='both')


#page6
ttk.Label(lst[5].get_modifiable_frame(), text='Rant Page', foreground='#faf7f7', background='green', font='Calibri 25').pack()
tk.Text(lst[5].get_modifiable_frame(), width=70, height=20).pack()
















lst[0].make_1st()
win.mainloop()
        
