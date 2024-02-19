import tkinter as tk

class app:
    def __init__(self,mainwindow):
        self.mainwindow = mainwindow

        tk.Label(mainwindow,text = 'Enter the Number: ').pack()

        self.num = tk.Entry(mainwindow)
        self.num.pack()

        tk.Button(mainwindow, text= "Enter",command = self.action).pack()

        self.out = tk.Label(self.mainwindow, text = '')
        self.out.pack()

        
    # Action
        
    def action(self):
        data = self.num.get()
        num = int(data)
        count = 0
        for i in range(2,num):
            if num % i == 0:
                count+=1
        if count == 0:
            self.out.config(text = 'prime Number!')
            self.out.pack()
        else:
            self.out.config(text = 'Not prime!')
            self.out.pack()

# main code
root = tk.Tk()
exe = app(root)
root.mainloop()