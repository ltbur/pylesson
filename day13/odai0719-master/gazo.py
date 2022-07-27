import tkinter as tk
from PIL import Image,ImageTk
import tkinter.ttk as ttk
import cv2,os
from opencv_japanese import imread
import imagehash
import tkinter.filedialog

img2             = ""
img3             = ""
img4             = ""

#['00.png',''],

gazo =[
    ['cry.png'  ,'ハカセ'],
    ['smile.png','ハカセ'],
    ['iroha.png','いろは（私）'],
    ['kaba1.jpg','コビトカバ'],
    ['kaba2.jpg','コビトカバ'],
    ['kaba3.jpg','コビトカバ'],
    ['cat1.png','ネコ'],
    ['cat2.jpg','ネコ'],
    ['cat3.jpg','ネコ'],
    ['01.png','レタス'],
    ['02.png','トマト'],
    ['03.png','パプリカ'],
    ['04.png','ピーマン'],
    ['05.png','トウモロコシ'],
    #['06.png','ナガネギ'],
    ['07.png','じゃがいも'],
    ['08.png','ラデッシュ'],
    ['09.png','さやえんどう'],
    ['10.png','じてんしゃ'],
    ['11.png','黄色い電車'],
    ['12.png','上からみた車'],
    ['13.png','テニスラケット'],
    ['14.png','野球のボール'],
    ['15.png','バレーのボール'],
    ['16.png','アメフトのボール?'],
    ['17.png','サッカーボール'],
    ['18.png','カレーライス'],
    ['19.png','えびフライ！'],
    ['20.png','スパゲティ'],
    ['21.png','おみそしる'],
    ['22.png','ころっけ'],
    ['23.png','ロールケーキ'],
    ['24.png','いちごのショートケーキ'],
    ['25.png','私の好きなミルクレープ'],
    ['26.png','パンダ'],
    ['27.png','ひよこさん'],
    ['28.png','シマリスさん'],
    ['29.png','アルパカ！！'],
    ['30.png','ぺんぎん'],
    ['31.png','なんか鳥'],
    ['32.png','ネズミ'],
    ['31.png','ヒョウ'],
    ['31.png','サーバルキャット'],
    ['31.png','お馬さん'],
    ['36.png','レッサーパンダ'], 
    ['37.png','きりんさん'],
    ['38.png','ネコさん'], 
    ['39.png','ネコさん'], 
    ['40.png','いぬ'],
    ['41.png','いぬ'], 
    ['42.png','青い鳥さん'],  
    ['43.png','ひよこさん'], 
]

def btn_click():
    global   img2,img3,img4
    input    =  entry.get()
    type     =  combobox.get()

    # 画像比べ処理
    hi_hit            =  0
    hi_hit_image      =  ""
    hi_hit_image_name =  ""

    if type == 'ヒストグラム比較':
        dirname  =  os.path.dirname(__file__)
        images1  =  imread(dirname + '\\' + input)
        #images1  =  imread(dirname + '\\images/' + input)     #テスト用にフォルダに入れたらにする

        #入力した画像のサイズ取得
        height = images1.shape[0]
        width  = images1.shape[1]
        img_size = (int(width), int(height))

        # 画像をヒストグラム化する（まず入力のみ）
        image1_hist = cv2.calcHist([images1], [2], None, [256], [0, 256])

    else:
        images1  =  Image.open(input)
        hash     =  imagehash.average_hash(images1)
        hi_hit   =  255                                        #適正なのか不明；
   
    #判定処理
    for i in range(len(gazo)):
        if type == 'ヒストグラム比較':
            images2  =  imread(dirname + '\\images/' + gazo[i][0])
            #入力画像に合わせてサイズを変更     
            image2 = cv2.resize(images2, img_size)
            # 画像をヒストグラム化する
            image2_hist = cv2.calcHist([image2], [2], None, [256], [0, 256])
            hit         = float(cv2.compareHist(image1_hist, image2_hist, 0))

            #print(hit)   #想像以上にレートが高い・・・

            if float(hi_hit) < float(hit):
                hi_hit            = hit
                hi_hit_image      = gazo[i][0]
                hi_hit_image_name = gazo[i][1]

        else:       #ハッシュ値変換比較
            images2    = Image.open('images/' + gazo[i][0])
            otherhash  = imagehash.average_hash(images2)            
            hit        = hash - otherhash

            if int(hi_hit) > int(hit):
                hi_hit            = hit
                hi_hit_image      = gazo[i][0]
                hi_hit_image_name = gazo[i][1] 

    #判定結果
    if type == 'ヒストグラム比較':
        rate = hi_hit * 100
    else:        
        rate = 100 - (hi_hit * 2)
        
    if (rate)    == 100:
        word  = 'これなら知ってます！'
        word2 = 'です！絶対！'
        img4 = Image.open('images/kira.png')
        img4 = img4.resize((128,96))
        img4 = ImageTk.PhotoImage(img4)
        canvas.create_image(225,200,image=img4,tag="emo")

    elif (rate)  >= 98:
        word  = 'あっ！これなら'
        word2 = 'だと思います！'
        canvas.delete("emo")
    else:
        img4 = Image.open('images/ase.png')
        img4 = img4.resize((80,80))
        img4 = ImageTk.PhotoImage(img4)
        canvas.create_image(210,170,image=img4,tag="emo")

        if (rate)  >= 90:
            word  = '多分なんですけど・・'
            word2 = 'とか・・かな。'
        
        elif (rate)  >= 75:
            word  = 'えっ・・・'
            word2 = 'みたいな・・？。'

        elif (rate)  >= 40:
            word =  'わからないですけど・・・'
            word2 = 'ですかね・・・ハハ。'
        else:
            word  ='・・・'
            word2 ='・・とか？'
        
    label3['text'] = '{}(判定結果値：{:.2f})'.format(word,rate)
    label4['text'] = '{}{}'.format(hi_hit_image_name,word2)

    img2_txt=tk.Label(root,text='～入力した画像～',font=('Arial',14),bg='pink')
    img2_txt.place(x=430,y=140)
    img2 = Image.open(input)
    img2_rx = float(300/img2.width)
    img2_ry = float(300/img2.height)
    img2 = img2.resize((int(img2.width*min(img2_rx,img2_ry)),int(img2.height*min(img2_rx,img2_ry))))
    img2 = ImageTk.PhotoImage(img2)
    canvas.create_image(525,320,image=img2)

    img3_txt=tk.Label(root,text='～イロハさんの回答～',font=('Arial',14),bg='pink')
    img3_txt.place(x=780,y=140)
    img3 = Image.open('images/' + hi_hit_image)
    img3_rx = float(300/img3.width)
    img3_ry = float(300/img3.height)
    #img3 = img3.resize((200,200))
    img3 = img3.resize((int(img3.width*min(img3_rx,img3_ry)),int(img3.height*min(img3_rx,img3_ry))))
    img3 = ImageTk.PhotoImage(img3)
    canvas.create_image(880,320,image=img3)

def func(): 
    f_path = tk.filedialog.askopenfilename(title="ファイル選択", initialdir="ディレクトリを入力", filetypes=[("Image file", ".bmp .png .jpg .jpeg .tif")])
    name = os.path.basename(f_path) 
    entry.delete( 0, tk.END )
    entry.insert( 0, name )

root=tk.Tk()
root.title('この画像は何？教えてイロハさん！')
root.resizable(False,False)
canvas = tk.Canvas(root,width=1200,height=800,bg='white')
canvas.pack()

img =tk.PhotoImage(file="images/iroha.png")
canvas.create_image(150,400,image=img)
 
fkd =tk.PhotoImage(file="images/fukidasi.png")
canvas.create_image(700,710,image=fkd)

#info =tk.Label(root,text='画像を入れるとイロハさんの「知ってる範囲」で何なのか教えてくれる・・・のだが・・・',font=('Arial',14),bg='white')
#info.place(x=300,y=40)
title = tk.PhotoImage(file="images/title.png")
canvas.create_image(650,80,image=title)

label=tk.Label(root,text='画像入力',font=('Arial',16))
label.place(x=330,y=480)

entry=tk.Entry(width=30)
entry.place(x=430,y=514)

btn2 = tkinter.Button(root, text="ファイル選択", command=func)
btn2.place(x=340,y=514)

btn=tk.Button(text='判定する',command=btn_click)
btn.place(x=630,y=512)

label3 = tk.Label(root,text='お好きな画像を選んでください。',font=('Arial',28),bg='white')
label3.place(x=330,y=600)

label4 = tk.Label(root,text='',font=('Arial',28),bg='white')
label4.place(x=330,y=650)

module = ('ヒストグラム比較', 'ハッシュ値変換比較')
v = tk.StringVar()
combobox = ttk.Combobox(root, textvariable= v, values=module, style="office.TCombobox")
combobox.current(0)
combobox.place(x=830,y=515)

root.mainloop()