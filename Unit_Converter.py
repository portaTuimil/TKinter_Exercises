import tkinter as tk
#from tkinter import ttk for default styles
import ttkbootstrap as ttk #overwrites the default styles

def convert():
    print(entryInt.get())
    output_string.set(entryInt.get() * 1.609)

window = ttk.Window(themename = 'darkly')
window.title('Unit Converter')
window.geometry('450x200')

title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack()

#Input:
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entryInt.set('')
entry = ttk.Entry(master = input_frame, textvariable = entryInt)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left')
button.pack(side = 'left')
input_frame.pack(padx=10)

#Output:
output_string = tk.StringVar()
output_label = ttk.Label(master = window, font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 10)

window.mainloop()
