"""
画板,鼠标移动速度太快可以造成不连续的点
tkinter 8.6.11
"""
from tkinter import Tk, Frame, Canvas, Button


penColor = "white"  # 画笔的颜色
backColor = "black"  # 画布背景色
penWidth = 20  # 笔刷的宽度


def paint(event):
    """在画板上绘制单个点"""
    global penWidth, canvas
    x1, y1 = (event.x, event.y)
    x2, y2 = (event.x + penWidth, event.y + penWidth)
    canvas.create_oval(x1, y1, x2, y2, fill=penColor, outline=penColor)


def cls():
    """将画板清空"""
    canvas.delete("all")


tk = Tk()

cco = Frame(tk)
cco.pack()


Omf = Frame(tk)
Omf.pack()


canvas = Canvas(tk, width=280, height=280, bg=backColor)
canvas.pack(expand=True, fill="both")

btn = Button(tk, text="clear", command=cls)
btn.pack()

canvas.bind("<B1-Motion>", paint)
canvas.mainloop()
