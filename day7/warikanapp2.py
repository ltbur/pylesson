import tkinter as tk
def bt_click():
    money=int(emoney.get())
    person=int(eperson.get())
    per=int((money/person)//100 * 100)
    if per*person < money:
        per +=100
    kanji=money-per*(person-1)
    lresult['text']=f'1人あたり{per}円({person-1}人)、幹事は{kanji}円です'
FNT=('sans-serif',10)
root=tk.Tk()
root.title('Warikan')
root.geometry('300x400')
root['bg']='skyblue'
lmoney=tk.Label(text='金額',font=FNT,bg='skyblue')
lmoney.pack(anchor=tk.W,padx=5,pady=5)
emoney=tk.Entry(width=20)
emoney.pack(anchor=tk.W,padx=5)
lperson=tk.Label(text='人数',font=FNT,bg='skyblue')
lperson.pack(anchor=tk.W,padx=5,pady=5)
eperson=tk.Entry(width=20)
eperson.pack(anchor=tk.W,padx=5)
btn=tk.Button(text='計算する',command=bt_click)
btn.pack(fill='x',padx=5,pady=20)
lresult=tk.Label(text='',font=FNT,bg='skyblue')
lresult.pack(anchor=tk.W,padx=5,pady=5)
root.mainloop()
