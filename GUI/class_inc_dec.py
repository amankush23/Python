'''Design and implement a simple counter application using Tkinter a python GUI lirary. 
The application should provide users with a graphical user interface featuring a counter
 lable and two  buttons for incrementing and devrementing the counter value. '''

import tkinter as tk
class counterApp:
    def __init__(self,mainwindow):
        self.mainwindow = mainwindow
        mainwindow.geometry('200x100')
        mainwindow.title("counter app")

        self.var = tk.IntVar(value=0)
        self.lb = tk.Label(mainwindow,textvar = self.var,font = 'BOLD')
        self.lb.pack()

        #Button

        bt1 = tk.Button(mainwindow,text=' Increment ', command = self.increment)
        bt1.pack(side = tk.LEFT)
        bt2 = tk.Button(mainwindow,text=' Decrement ', command = self.decrement)
        bt2.pack(side = tk.RIGHT)
        # action1

'''def my_fun1():
    data = lb.cget('text')
    data+=1
    lb.config(text=data, fg='red')
def my_fun2():
    lb.config(text=lb.cget('text')-1)'''

# action2

def increment(self):
    data = self.var.get()
    self.var.set(data+1)
    if data>= 10:
        self.lb.config(fg='red')
    else:
        self.lb.config(fg = 'blue')
def decrement(self):
    data = self.var.get()
    self.var.set(data-1)
    if data <= -10:
        self.lb.config(fg='red')
    else:
        self.lb.config(fg = 'blue')


#Display
root = tk.Tk()
exc = counterApp(root)
root.mainloop()

