import tkinter as tk

root = tk.Tk()
root.title("マップデータ")
canvas = tk.Canvas(width=335, height=240)
canvas.pack()
img = [
        tk.PhotoImage(file="chip0"),
        tk.PhotoImage(file="chip1"),
        tk.PhotoImage(file="chip2"),
        tk.PhotoImage(file="chip3")
        ]
map_data = [
        [0,1,0,2,2,2,2],
        [3,0,0,0,2,2,2],
        [3,0,0,1,0,0,0],
        [3,3,0,0,0,0,1],
        [3,3,3,3,0,0,0]
        ]
for y in range(5):
    for x in range(7):
        n = map_data[y][x]
        canvas.create_image(x*48+24, y*48+24, image=img[n])
root.mainloop()
