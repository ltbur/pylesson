import tkinter as tk
def bt_click():
	amount=int(amount_et.get())
	people=int(people_et.get())
	dnum=amount/people
	pay=int(dnum // 100 *100)
	if dnum > pay:
		pay+=100
	payorg=amount-pay*(people-1)
	resutl_label['text']='1人あたり{}円({}人)、幹事は{}円です'.format(pay,people-1,payorg)

root = tk.Tk()
root.title("割り勘くん")
root.resizable(False, False)
canvas = tk.Canvas(root, width=400, height=600,bg='skyblue')
canvas.pack()
amount_label=tk.Label(text='金額',font=("Arial", 16),bg='skyblue')
amount_label.place(x=10,y=20)
amount_et=tk.Entry(width=20)
amount_et.place(x=10,y=50)
people_label=tk.Label(text='人数',font=("Arial", 16),bg='skyblue')
people_label.place(x=10,y=90)
people_et=tk.Entry(width=20)
people_et.place(x=10,y=120)
btn=tk.Button(text='計算する',font=("Arial",20),command=bt_click)
btn.place(x=10,y=190)
resutl_label=tk.Label(text='',font=("Arial",18),bg='skyblue')
resutl_label.place(x=10,y=240)
root.mainloop()
