import pandas as pd
import random
import tkinter as tk

def b1_click():
    count=0;
    word=e1.get()
    for w in words:
        if (word in w):
            count +=1
    t1.insert(tk.END,'{}:{}回\n'.format(word,count))
    e1.delete(0, tk.END)
def b2_click():
    ans=e2.get()
    if(ans==titles_name[idx]):
        t2.insert(tk.END,f'「{ans}」……正解！！\n')
    else:
        t2.insert(tk.END,f'「{ans}」は違うよ\n')

titles=[
    "ginga.csv",
    "sero.csv",
    "neko.csv",
    "tyuumon.csv",
    "kokoro.csv",
    "kumo.csv",
    "rasyou.csv",
    "gon.csv",
    "sangetu.csv",
    "kapa.csv",
    "merosu.csv",
    "hana.csv",
    "toshi.csv",
    "toro.csv",
    "bochan.csv",
    "yamanasi.csv",
    "takase.csv",
    "maihime.csv",
    "kani.csv",
    "kazeno.csv"
]
titles_name=[
    "銀河鉄道の夜",
    "セロ弾きのゴーシュ",
    "吾輩は猫である",
    "注文の多い料理店",
    "こころ",
    "蜘蛛の糸",
    "羅生門",
    "ごんぎつね",
    "山月記",
    "河童",
    "走れメロス",
    "鼻",
    "杜子春",
    "トロッコ",
    "坊ちゃん",
    "やまなし",
    "高瀬舟",
    "舞姫",
    "蟹工船",
    "風の又三郎"
]

idx=random.randint(0,len(titles)-1)
df = pd.read_csv(titles[idx])
words=df.iloc[:,3]

root=tk.Tk()
root.title('クイズ')
root.geometry('1200x800')
canvas=tk.Canvas(root,width=1200,height=800,bg='skyblue')
canvas.pack()


img=tk.PhotoImage(file='hakase1_smile.png')
img = img.subsample(6)
canvas.create_image(50,50,image=img)

l0=tk.Label(root,text='ワシが選んだ小説のタイトルを当てるんじゃ！',font=('Arial',30),bg='skyblue')
l0.place(x=100,y=30)

l1=tk.Label(root,text='登場回数を調べたい単語↓',font=('Arial',20))
l1.place(x=50,y=100)
t1=tk.Text(width=25,height=400,font=("Times New Roman", 16),bg='skyblue')
t1.place(x=400,y=100)
e1=tk.Entry(width=20,font=("Times New Roman", 16))
e1.place(x=50,y=150)
b1=tk.Button(width=10,height=3,text='回数を検索',command=b1_click)
b1.place(x=50,y=180)
l2=tk.Label(root,text='タイトルを回答↓',font=('Arial',20))
l2.place(x=50,y=270)
e2=tk.Entry(width=20,font=("Times New Roman", 16))
e2.place(x=50,y=320)
b2=tk.Button(width=10,height=3,text='回答',command=b2_click)
b2.place(x=50,y=360)
t3=tk.Text(width=20,height=400,font=('Arial',20),bg='skyblue')
t3.place(x=700,y=100)
t2=tk.Text(width=20,height=40,font=("Times New Roman", 16),bg='skyblue')
t2.place(x=50,y=420)

t3.insert(tk.END,'【選択肢】\n')
for t in titles_name:
    t3.insert(tk.END,f'{t}\n')


root.mainloop()
