from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Google Trends Scraper')
# root.iconbitmap('./')
root.geometry('300x100')

e =Entry(root, width=35, borderwidth=5)
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
e.insert(0, 'Enter number of days to collect')
# e.bind(sequence, func)

def validate_input():
    global days
    while True:
        try:
            days = int(e.get())
        except ValueError:
            messagebox.showerror('Wrong Input', 'Kindly key in a number')
            break
        if days == 0:
            messagebox.showwarning('Wrong Input', 'Your response must be greater than zero')
            break
        else:
            break
    
Button(root, text='Collect', command=validate_input).grid(row=2, column=1, padx=10, pady=5)

root.mainloop()