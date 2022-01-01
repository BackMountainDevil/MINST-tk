"""
画板：测试画点十分凌乱且难以连成线
matplotlib  3.5.0
"""
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
plt.axis("off")  # 关闭坐标轴
# plt.ion() # 开启交互式功能，开启了在我的电脑上无法运行


def on_move(event):
    """鼠标移动处理：左键按下就画点"""
    if event.inaxes:
        # print('data coords %f %f' % (event.xdata, event.ydata))
        if event.button is MouseButton.LEFT:
            plt.scatter(event.xdata, event.ydata, c="black")  # 绘制散点
            plt.show()


plt.connect("motion_notify_event", on_move)
plt.show()
