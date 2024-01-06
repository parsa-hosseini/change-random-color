from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('800x600')
win.resizable(0 , 0)
win.title('color')
def change_color():
    import random as r
    lst = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = f'#{r.choice(lst)}{r.choice(lst)}{r.choice(lst)}{r.choice(lst)}{r.choice(lst)}{r.choice(lst)}'
    win.configure(bg = color)
    lac.configure(text = color)
def exit_app():
    x = messagebox.askyesno('warning' , 'Are you sure to exit?')
    if x == True:
        win.destroy()
la1 = Label(win , text = 'Parsa Hosseini' , bg = 'light green' , fg = 'black' ,font = '300')
la1.place(x = 350 , y = 200)
lac = Label(text = 'Empty' , fg = 'black' , bg = 'gray' , font = '200')
lac.place(x = 375 , y = 250)
btn1 = Button(win , text = "^_^" , bg = 'black' , fg = 'light green' , font = '200' , command = change_color)
btn1.place(x = 380 , y = 300)
btn2 = Button(text = 'Exit' , bg = 'white' , fg = 'black' , font = '200' , command = exit_app)
btn2.place(x = 380  , y = 350)
win.mainloop()