import tkinter as tk
import ttkbootstrap as ttk

def convert(entry_var):
    output_string.set(round(entry_var.get() * 1.61, 2))
    #new_window = ttk.Window(title='Hello')
    #new_window.geometry('300x150')
    #new_window.mainloop()





# window
window = tk.Tk()
window.title('Demo')
window.geometry('300x150')

# title
title_label = ttk.Label(window, text='Miles to kilometres', font='Calibri 20')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=lambda: convert(entry_int))
entry.pack(side='left')
button.pack(side='right', padx=10)

button2 = ttk.Button(master=input_frame, text='Test')
button2.pack(side='right')

input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='Output', font='Calibri 24', textvariable=output_string)
output_label.pack(pady=5)

window.mainloop()



