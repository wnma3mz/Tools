# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

# https://www.bilibili.com/video/av82339238?t=164&p=2


def caluate_point(point, vertex, trials):
    direction_arr = np.random.choice(len(vertex), trials, p=p_lst)
    direction_arr = np.array(list(map(lambda i: vertex[i], direction_arr)))
    point_lst = []
    for direction in direction_arr:
        point = tuple((p / step1 + d / step2) for p, d in zip(point, direction))
        point_lst.append(point)
    return point_lst

if __name__ == '__main__':
    # 迭代次数
    trials = 10000
    step = 2
    step1, step2 = step, step
    # 指定N个顶点
    N = 4
    max_x = 1000
    vertex = [(0, 0)]
    if N == 3:
        vertex.append((max_x, 0))
        vertex.append((max_x / 2, np.sqrt(max_x ** 2 - (max_x / 2)** 2)))
    elif N == 4:
        vertex.append((max_x, 0))
        vertex.append((0, max_x))
        vertex.append((max_x, max_x))

    N = len(vertex)
    # 每个变换的执行概率
    # p_lst = [0.4, 0.3, 0.2, 0.1]
    p_lst = np.array([1 / N]*N)

    max_value = np.max(vertex)
    x = np.random.randint(max_value)
    y = np.random.randint(max_value)
    point = (x, y)

    # 三角形顶点
    x, y = zip(*vertex)
    plt.scatter(x, y, color='black')
    plt.scatter(*point, color='red')


    point_lst = caluate_point(point, vertex, trials)
    x, y = zip(*point_lst)
    plt.scatter(x, y, color='blue', s=1, marker='.')

    plt.show()
