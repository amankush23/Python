import tkinter as tk
# other form ==> from tkinter import *

#Root
root = tk.Tk()
root.geometry('200x100')
root.title('First App')
root.minsize(100,50)

# def my_fun():
#     data = lb.cget('text')
#     if data == "Hi":
#         lb.config(text = 'Hello')
#     else:
#         lb.config(text = 'Hi')

def my_fun1():
    data = lb.cget('text')
    data+=1
    lb.config(text=data, fg='red')
def my_fun2():
    lb.config(text=lb.cget('text')-1)
lb = tk.Label(root,text=0)
lb.pack()

bt1 = tk.Button(root,text=' + ', command = my_fun1)
bt1.pack()
bt2 = tk.Button(root,text=' - ', command = my_fun2)
bt2.pack()

root.mainloop()
