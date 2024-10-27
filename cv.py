import cv2
import os
import matplotlib.pyplot as plt

# 图像路径
image_path = '1.jpg'

# 检查文件是否存在
if not os.path.isfile(image_path):
    print("错误：图像文件不存在，请检查路径。")
else:
    # 读取图片
    image = cv2.imread(image_path)

    # 检查图像是否成功加载
    if image is None:
        print("错误：图像加载失败，可能是文件格式不支持或文件损坏。")
    else:
        # 转换 BGR 到 RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 使用 matplotlib 显示图像
        plt.imshow(image)
        plt.axis('off')  # 不显示坐标轴
        plt.show()

