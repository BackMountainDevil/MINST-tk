"""
使用已经训练好的模型预测手写数字
paddlepaddle  2.2.1
"""
import numpy as np
import paddle.fluid as fluid
from PIL import Image
from paddle.fluid.dygraph import Linear


class multilayer_perceptron(fluid.dygraph.Layer):
    """动态图定义多层感知器"""

    def __init__(self):
        super(multilayer_perceptron, self).__init__()
        self.fc1 = Linear(input_dim=28 * 28, output_dim=100, act="relu")
        self.fc2 = Linear(input_dim=100, output_dim=100, act="relu")
        self.fc4 = Linear(input_dim=100, output_dim=100, act="relu")
        self.fc3 = Linear(input_dim=100, output_dim=10, act="softmax")

    def forward(self, input_):
        x = fluid.layers.reshape(input_, [input_.shape[0], -1])
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc4(x)
        y = self.fc3(x)
        return y


def load_image(file):
    """对图片进行预处理"""
    im = Image.open(file).convert("L")  # 将RGB转化为灰度图像，L代表灰度图像，像素值在0~255之间
    im = im.resize((28, 28), Image.ANTIALIAS)  # 修改图像大小为28*28
    im = (
        np.array(im).reshape(1, 1, 28, 28).astype(np.float32)
    )  # 返回新形状的数组,把它变成一个 numpy 数组以匹配数据馈送格式。
    im = im / 255.0 * 2.0 - 1.0  # 归一化到【-1~1】之间
    return im


infer_path = "work/8.png"
img = Image.open(infer_path)

# 构建预测动态图过程
label_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
model_path = "work/model"  # 模型路径
with fluid.dygraph.guard():
    model = multilayer_perceptron()  # 模型实例化
    model_dict, _ = fluid.load_dygraph(model_path)
    model.load_dict(model_dict)  # 加载模型参数
    model.eval()  # 评估模式
    infer_img = load_image(infer_path)
    infer_img = np.array(infer_img).astype("float32")
    infer_img = infer_img[np.newaxis, :, :, :]
    infer_img = fluid.dygraph.to_variable(infer_img)
    result = model(infer_img)
    print("infer results: %s" % label_list[np.argmax(result.numpy())])
