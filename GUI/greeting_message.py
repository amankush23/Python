import tkinter as tk

class app:
    def __init__(self,mainwindow):
        self.mainwindow = mainwindow

        tk.Label(mainwindow,text = 'Enter the Name: ').pack()

        self.name = tk.Entry(mainwindow)
        self.name.pack()

        tk.Button(mainwindow, text= "Enter",command = self.action).pack()

        self.out = tk.Label(mainwindow, text = '')
        self.out.pack()

    def action(self):
        data = self.name.get()
        self.out.config(text='Hello '+data)
        self.name.delete(0,tk.END)

        
# main code
root = tk.Tk()
exe = app(root)
root.mainloop()