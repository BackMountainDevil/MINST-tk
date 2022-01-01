"""
画板,鼠标移动速度太快可以造成不连续的点
tkinter 8.6.11
https://stackoverflow.com/questions/17915440/python-tkinter-save-canvas-as-image-using-pil
"""
import tkinter as tk
from PIL import Image, ImageDraw


class ImageGenerator:
    def __init__(self, parent, posx, posy, *kwargs):
        self.parent = parent
        self.posx = posx
        self.posy = posy
        self.sizex = 280
        self.sizey = 280
        self.penColor = "white"  # 画笔的颜色 (255, 255, 255)
        self.backColor = "black"  # 画布背景色 (0, 0, 0)
        self.penWidth = 10  # 笔刷的宽度
        self.drawing_area = tk.Canvas(
            self.parent, width=self.sizex, height=self.sizey, bg=self.backColor
        )
        self.drawing_area.place(x=self.posx, y=self.posy)
        self.drawing_area.bind("<B1-Motion>", self.motion)
        self.button = tk.Button(
            self.parent, text="Done", width=10, bg="white", command=self.save
        )
        self.button.place(x=self.sizex / 7, y=self.sizey + 20)
        self.button1 = tk.Button(
            self.parent, text="Clear", width=10, bg="white", command=self.clear
        )
        self.button1.place(x=(self.sizex / 7) + 80, y=self.sizey + 20)

        self.image = Image.new("RGB", (self.sizex, self.sizey), (0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)

    def save(self):
        filename = "temp.jpg"
        self.image.save(filename)

    def clear(self):
        """将画板和image清空"""
        self.drawing_area.delete("all")
        self.image = Image.new("RGB", (self.sizex, self.sizey), (0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)

    def motion(self, event):
        """在画板和image上同时绘制"""
        self.drawing_area.create_oval(
            event.x,
            event.y,
            event.x + self.penWidth,
            event.y + self.penWidth,
            fill=self.penColor,
            outline=self.penColor,
        )  # 在画布上画

        self.draw.ellipse(
            (
                (event.x, event.y),
                (event.x + self.penWidth, event.y + self.penWidth),
            ),
            fill=self.penColor,
            outline=self.penColor,
            width=self.penWidth,
        )  # 在生成的图上画,point、line都太细


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_geometry("%dx%d+%d+%d" % (300, 350, 10, 10))
    root.config(bg="white")
    ImageGenerator(root, 10, 10)
    root.mainloop()
