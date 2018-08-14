# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 迭代次数
N = 100
# 粒子个数,种群规模
n = 100
# 粒子更新公式:
# v[i] = w * v[i] + c1*rand()*(pbest[i]-x[i])+c2*rand()*(gbest-x[i])
# x[i] += v[i]
# 学习因子（加速常数）
c1 = 0.2
c2 = 0.2
# w为惯性因子
w = 0.8
# 范围
X_BOUND = [0, 5]


def F(x):
    # 目标函数，找最值，范围0，5
    return np.sin(10 * x) * x + np.cos(2 * x) * x


def find():

    # 初始化n个粒子组成的群落
    x = np.random.rand(n) * 5
    # 初始化每个粒子的飞行速度
    v = np.random.rand(n)
    # vmax粒子最大的飞行速度
    vmax = 0.2
    # 每个粒子目前为止搜索到的最优位置，个体极值
    pbest = F(x)
    # 整个粒子群搜索到的最优位置，全局极值
    gbest = 0, -10000

    for t in range(N):
        v = w * v + c1 * np.random.rand() * (pbest - x) + c2 * \
            np.random.rand() * (gbest[1] - x)
        v = np.where(v > vmax, vmax, v)
        v = np.where(v < -vmax, -vmax, v)
        x += v
        # 越界判断
        x = np.where(x < X_BOUND[0], X_BOUND[0], x)
        x = np.where(x > X_BOUND[1], X_BOUND[1], x)
        for i in range(n):
            pbest[i] = max(F(x[i]), pbest[i])
            if (F(x[i]) > gbest[1]):
                gbest = x[i], F(x[i])
        # print(gbest)
        yield gbest
    # print(x, gbest)


if __name__ == '__main__':
    # 绘制底板
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = np.linspace(*X_BOUND, 200)
    # 绘制函数图像
    plt.plot(x, F(x))
    # find()
    line, = ax.plot([], [], 'bo', ms=10)

    def simPoints(simData):
        x, y = simData[0], simData[1]
        line.set_data(x, y)
        return line
    # 使用这个函数，fig是本身的画板，simPoints是需要绘制的点，simData是产生数据的函数传递给simPoints，interval动画间隔时间，单位是ms
    ani = animation.FuncAnimation(
        fig, simPoints, find, interval=200)

    plt.show()
