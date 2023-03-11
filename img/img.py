from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math


# 1. 查看 --> 使用matplotlib显示一张图片
def show_img(filepath: str):
    # 1. 读取图片
    img = Image.open(filepath)
    img = np.array(img)
    # 2. 获取文件名，作为标题显示
    # -> 两种斜杠混用也不怕
    start_1 = filepath.rfind('/')
    start_2 = filepath.rfind('\\')
    start = max(start_1, start_2)
    filename = filepath[start+1:]
    # 3. 画出图片
    plt.rc('font', family='KaiTi')
    plt.figure(figsize=(16, 16))
    f = plt.subplot(111)
    f.set_title(filename, fontsize=20)
    plt.imshow(img)
    plt.show()


# 2. 查看 --> 使用matplotlib显示list中所有图片
def show_imgs(filepaths: list):
    # 1. 读取图片
    # 2. 获取文件名
    imgs = []
    filenames = []
    for filepath in filepaths:
        img = Image.open(filepath)
        img = np.array(img)
        imgs.append(img)

        start_1 = filepath.rfind('/')
        start_2 = filepath.rfind('\\')
        start = max(start_1, start_2)
        filename = filepath[start+1:]
        filenames.append(filename)
    # 3. 画出图片
    plt.rc('font', family='KaiTi')
    plt.figure(figsize=(16, 16))
    f_size = int(math.sqrt(len(filepaths))) + 1  # 自动根据图片数量调整布局
    for i, img in enumerate(imgs):
        f = plt.subplot(f_size, f_size, i + 1)
        f.set_title(filenames[i], fontsize=10)
        plt.imshow(img)
    plt.show()



if __name__ == "__main__":
    # 1. 查看 --> 使用matplotlib显示一张图片
    filepath = 'C:\\Users\\ThinkPad\\Desktop/洛谷.png'
    filepath_2 = 'C:\\Users\\ThinkPad\\Desktop/邻域榜_软件工程第1.png'
    show_img(filepath=filepath)

    # 2. 查看 --> 使用matplotlib显示list中所有图片
    filepaths = []
    filepaths.append(filepath)
    filepaths.append(filepath_2)
    show_imgs(filepaths=filepaths)