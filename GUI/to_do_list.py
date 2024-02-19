import tkinter as tk 

class todo:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.mainwindow.geometry('500x400')

        def add():
            data  = self.add_items.get()
            self.List_box.insert(tk.END, data)
            self.add_items.delete(0,tk.END)
        def delete_item():
            index = self.List_box.curselection()
            self.List_box.delete(index)
        def delete_all_items():
            self.List_box.delete(0, tk.END)

        self.add_items =  tk.Entry(self.mainwindow, text = "")
        self.add_items.grid(row = 0 , column= 0 )

        self.b1 = tk.Button(self.mainwindow, text = 'Add Items', command = add, bg = 'red')
        self.b1.grid(row = 0 , column=1)
        

        self.List_box = tk.Listbox(self.mainwindow, width = 30)
        self.List_box.grid(row = 1, column=0 )

        self.b2 = tk.Button(self.mainwindow, text = "Delete" , command= delete_item,bg = 'green')
        self.b2.grid(row = 3,column= 0 )

        self.b3 = tk.Button(self.mainwindow, text = "delete_all_items" , command= delete_all_items, bg = 'yellow')
        self.b3.grid(row = 3,column= 1 )

root = tk.Tk()
exe = todo(root)
root.mainloop()


        
        
