'''Design and implement a simple counter application using Tkinter a python GUI lirary. 
The application should provide users with a graphical user interface featuring a counter
 lable and two  buttons for incrementing and devrementing the counter value. '''

import tkinter as tk


#root = main window

root = tk.Tk()
root.geometry('200x100')
root.title("counter app")
#global initialization
var = tk.IntVar(value=0)

# action1

'''def my_fun1():
    data = lb.cget('text')
    data+=1
    lb.config(text=data, fg='red')
def my_fun2():
    lb.config(text=lb.cget('text')-1)'''

# action2

def increment():
    data = var.get()
    var.set(data+1)
    if data>= 10:
        lb.config(fg='red')
    else:
        lb.config(fg = 'blue')
def decrement():
    data = var.get()
    var.set(data-1)
    if data <= -10:
        lb.config(fg='red')
    else:
        lb.config(fg = 'blue')

# Lable
        
lb = tk.Label(root,textvariable = var,font = 'BOLD' )
lb.pack()

#Button

bt1 = tk.Button(root,text=' Increment ', command = increment)
bt1.pack(side = tk.LEFT)
bt2 = tk.Button(root,text=' Decrement ', command = decrement)
bt2.pack(side = tk.RIGHT)

#Display

root.mainloop()
