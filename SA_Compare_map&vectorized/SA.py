# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation
# 初始温度
T = 100
# 最低温度
T_min = 1e-8
# 解个数
k = 100
# 温度下降率
delta = 0.98
X_BOUND = [0, 5]


def F(x):
    # 目的：找到下面这个函数的最值
    return np.sin(10 * x) * x + np.cos(2 * x) * x


def move(num, tnum):
    Fnum = F(num)
    x_new = num + (np.random.rand() * 2 - 1) * tnum
    if (0 <= x_new and x_new <= 5):
        Fnum_new = F(x_new)
        if (Fnum_new < Fnum):
            return x_new
        else:
            p = 1 / (1 + np.exp(-(Fnum_new - Fnum) / T))
            if (np.random.rand() < p):
                return x_new
    return num


def move2(num, t):
    Fnum = F(num)
    x_new = num + (np.random.rand() * 2 - 1) * t
    if (0 <= x_new and x_new <= 5):
        Fnum_new = F(x_new)
        if (Fnum_new < Fnum):
            return x_new
        else:
            p = 1 / (1 + np.exp(-(Fnum_new - Fnum) / T))
            if (np.random.rand() < p):
                return x_new
    return num


def getSA():
    # 初始化初始解
    x = np.random.random(k) * (X_BOUND[1] - X_BOUND[0])
    t = T
    # 开始退火
    while (t > T_min):
        # 对每个可能值进行移动
        for i, num in enumerate(x):
            Fnum = F(num)
            # 左右移动的范围，由自己决定
            x_new = num + (np.random.rand() * 2 - 1)
            # 保证移动后的范围在区间内
            if (0 <= x_new and x_new <= 5):
                # 移动后的值
                Fnum_new = F(x_new)
                # 寻找最小值。如果新值小于原来的值，那么就进行替换
                if (Fnum_new < Fnum):
                    # 寻找最大值。如果新值大于原来的值，那么就进行替换
                    # if (Fnum_new > Fnum):
                    x[i] = x_new
                else:
                    # 为了避免陷入局部最优，以一个概率来决定是否进行移动。公式是固定的。
                    p = 1 / (1 + np.exp(-(Fnum_new - Fnum) / T))
                    if (np.random.rand() < p):
                        x[i] = x_new
        # 每次退火的比率
        t *= delta
        # print("x坐标：{}, y坐标：{}".format(x[np.argmin(F(x))], np.min(F(x))))
        yield x[np.argmin(F(x))], np.min(F(x))
    # return x[np.argmax(F(x))], np.max(F(x))


def test_map():
    x = np.random.random(k)
    t = T
    while (t > T_min):
        x = list(map(move, x, [t] * k))
        t *= delta
    return x


def test_vectorized():
    x = np.random.random(k)
    t = T
    move2f = np.vectorize(move2)
    while (t > T_min):
        x = move2f(x, t)
        t *= delta
    return x


def simPoints(simData):
    x, y = simData[0], simData[1]
    line.set_data(x, y)
    return line


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.linspace(*X_BOUND, 200)
    plt.plot(x, F(x))
    line, = ax.plot([], [], 'bo', ms=10)
    ani = animation.FuncAnimation(
        fig, simPoints, getSA, interval=400)

    # x = test_vectorized()
    # print("x坐标：{}, y坐标：{}".format(x[np.argmin(F(x))], np.min(F(x))))
    # x = np.array(test_map())
    # print("x坐标：{}, y坐标：{}".format(x[np.argmin(F(x))], np.min(F(x))))
    # x = getSA()
    plt.show()
    # print("x坐标：{}, y坐标：{}".format(x[np.argmax(F(x))], np.max(F(x))))
