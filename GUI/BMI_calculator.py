import tkinter as tk

root = tk.Tk()
root.geometry('400x300')
root.title('BMI calculator')

def calculate():
    weight = float(entry1.get())
    height = float(entry2.get())
    result =  weight /  (height**2)
    lb3.config(text = result )
    
lb1= tk.Label(root, text = "Enter the Weight: ")
lb1.grid(row = 0, column=0)
entry1= tk.Entry(root)
entry1.grid(row = 0, column=1)
lb2= tk.Label(root, text = "Enter the Height: ")
lb2.grid(row = 1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row = 1 , column=1)
lb3= tk.Label(root, width = 20)
lb3.grid(row = 2, column=0)

b1 = tk.Button(root,text = 'Button' ,command = calculate)
b1.grid(row = 5, column=1)
root.mainloop()