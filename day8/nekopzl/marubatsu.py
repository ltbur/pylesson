import tkinter as tk
import random

index = 0 #ゲーム進行index
timer = 0 #ゲームオーバー時に1秒間止める際に必要
turn = 0 #ターン
colIndex = 0 #colIndex(0-2)
rowIndex = 0 #rowIndex(0-2)
mouse_x = 0 #マウスのx座標
mouse_y = 0 #マウスのy座標
mouse_c = 0 #クリック管理(0,1)

#マウスの座標をグローバル変数に入れる
def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

#マウスが押されたときにmouse_cを１
def mouse_press(e):
    global mouse_c
    mouse_c = 1

neko = [] #現在の盤面を管理する配列(3行3列)
check=[] # check用
#２つの配列を初期化
for i in range(3):
    neko.append([0,0,0])
    check.append([0,0,0])

#現在の盤面をもとにネコを描画
def draw_neko():
    cvs.delete("NEKO")
    for y in range(3):
        for x in range(3):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag="NEKO")

#判定(縦横斜めに３つ以上並んだところを肉球(3)にする)
def check_neko():
    for y in range(3):
        for x in range(3):
            #現在の盤面をチェック用配列にコピー
            check[y][x] = neko[y][x]

    #縦に３つ並んだかの判定
    for x in range(3):
        if check[1][x] > 0:
            if check[0][x] == check[1][x] == check[2][x] :
                neko[0][x] =  neko[1][x] =  neko[2][x] = 3

    #横に３つ並んだかの判定
    for y in range(3):
        if check[y][1] > 0:
            if check[y][0] == check[y][1] == check[y][2] :
                neko[y][0] =  neko[y][1] =  neko[y][2] = 3

    #斜めに３つ並んだかの判定
        if check[1][1] > 0:
            #\ラインの判定
            if check[0][0] == check[1][1] == check[2][2]:
                neko[0][0] =  neko[1][1] =  neko[2][2] = 3
            #/ラインの判定
            if check[2][0] == check[1][1] == check[0][2]:
                neko[2][0] =  neko[1][1] =  neko[0][2] = 3

#肉球が何個あったかを返す関数
def count_niku():
    num = 0
    for y in range(3):
        for x in range(3):
            if neko[y][x] == 3:
                num += 1
    return num

#文字列を表示する関数
def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    #影設定
    cvs.create_text(x+1, y+1, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def game_main():
    global index, timer, turn
    global colIndex, rowIndex, mouse_c
    if index == 0: # タイトルロゴ
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("ゲームスタート", 312, 420, 20, "white", "TITLE")
        index = 1
        turn=0
        mouse_c = 0
    elif index == 1: # タイトル画面 スタート待ち
        if mouse_c == 1 and  168 < mouse_x < 456 and 384 < mouse_y < 456:
            for y in range(3):
                for x in range(3):
                    neko[y][x] = 0
            mouse_c = 0
            colIndex = 0
            rowIndex = 0
            draw_neko()
            cvs.delete("TITLE")
            index = 2
    elif index == 2: 
        if 24 <= mouse_x < 24+72*3 and 24 <= mouse_y < 24+72*3:
            cvs.delete("CURSOR")
            cvs.create_image(colIndex*72+60, rowIndex*72+60, image=cursor, tag="CURSOR")
            colIndex = int((mouse_x-24)/72)
            rowIndex = int((mouse_y-24)/72)
            if mouse_c == 1:
                #すでに猫があったら何もしない
                if neko[rowIndex][colIndex] > 0:
                    pass
                else:
                    neko[rowIndex][colIndex] = 1 if turn % 2==0 else 2 #クリックした場所に次の猫をおく
                    turn += 1
                    index=3
                mouse_c = 0
    elif index == 3: # 判定
        check_neko() #揃った場所に3をいれる
        draw_neko() #描画（3の場所は肉球)
        if count_niku()== 0 and turn != 9:
            index = 2
        else:
            index = 4
            timer = 0
        draw_neko()
    elif index == 4: # ゲームオーバー
        timer += 1
        if timer == 1:
            msg=str()
            if count_niku()== 0 and turn == 9:
                msg="Draw"
            elif turn % 2 == 0:
                msg="P2 Win!"
            else:
                msg="P1 Win!"
            draw_txt(msg, 312, 348, 60, "red", "OVER")
        if timer == 10:
            cvs.delete("OVER")
            index = 0
    #100m秒ごとにgame_mainを繰り返す（心臓)
    root.after(100, game_main)

root = tk.Tk()
root.title("「ねこ x ねこ」")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
cvs = tk.Canvas(root, width=912, height=768)
cvs.pack()

bg = tk.PhotoImage(file="neko_bg.png")
cursor = tk.PhotoImage(file="neko_cursor.png")
img_neko = [
    None,
    tk.PhotoImage(file="neko1.png"),
    tk.PhotoImage(file="neko2.png"),
    tk.PhotoImage(file="neko_niku.png")
]
cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()
