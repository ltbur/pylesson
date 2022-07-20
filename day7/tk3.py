import tkinter as tk
root=tk.Tk()
root.title('My Window')
root.geometry('600x400')

label=tk.Label(root,text='Hello World!',font=('Arial',50))
label.place(x=100,y=100)
root.mainloop()
