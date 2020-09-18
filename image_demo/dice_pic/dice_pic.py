# coding: utf-8
from PIL import Image
import numpy as np


im = Image.open('0.jpg')
im_array = np.array(im)


def six_step_gray(x):
    # 将一个数值区间内的像素值，转换为指定像素
    for i in range(15):
        if (i * 17 <= x < i * 17 + 17):
            return i * 17 + 17
    return 255


def split_val(box, dice_num):
    for i1 in range(box[0], box[2] + 1):
        for j1 in range(box[1], box[3] + 1):
            im_array[j1, i1, :] = dice_num


if __name__ == '__main__':
    # 整数1表骰子朝上有1个白点，如果数字越小区域越黑，白点越多，区域越白。
    # 区域划分越小，模拟图效果越好
    num = 7  # 不能被图片的长或宽整除
    pic_width, pic_heigth = im.size

    # 将图片分为 num x num
    for i in range(int(pic_width / num)):
        for j in range(int(pic_heigth / num)):
            # 裁剪
            box = (i * num, j * num, i * num + num, j * num + num)
            patch = im.crop(box)
            # 转化为灰度图
            pL = patch.convert('L')
            # 取出数组的平均值，转换
            dice_num = six_step_gray(np.mean(pL))
            # 赋值
            split_val(box, dice_num)

    # 重新转换为图片
    im_new = Image.fromarray(im_array)
    im_new.show()
    im_new.save('1.png')
