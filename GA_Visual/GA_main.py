# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
# GA——遗传算法，SA模拟退火算法
# 每个个体序列长度
DNA_SIZE = 10
# 种群个体数目
POP_SIZE = 100
# 交叉配对比例
CROSS_RATE = 0.8
# 变异概率
MUTATION_RATE = 0.003
# 进化次数，迭代次数
N_GENERATIONS = 100
# 数据范围
X_BOUND = [0, 5]


def F(x):
    # 目的：找到下面这个函数的最值
    # sin(10x)*x+cos(2x)*x
    return np.sin(10 * x) * x + np.cos(2 * x) * x


def get_fitness(pred):
    # 函数中每个值减去最小值（表现最差的个体），加上允许误差值0.001
    # 找到函数中的最大值
    return pred - np.min(pred) + 1e-3
    # 找到函数中的最小值
    # return np.max(pred) - pred + 1e-3


def translateDNA(pop):
    # 将个体中DNA转换为所需的数据（二进制换为十进制），并且归一化到指定范围（这里是[0，5]）
    # 二进制转十进制的范围是2^DNA_SIZE-1=1023，转换到指定范围*(5-0)
    return np.dot(pop, 2**np.arange(DNA_SIZE)[::-1] * 1.0 / (2**DNA_SIZE - 1) * (X_BOUND[1] - X_BOUND[0]))


def select(pop, fitness_score):
    # 进行筛选
    # 从np.arange(POP_SIZE)选出POP_SIZE个，replace=True可重复选择，p表示每项的适应度（选中的概率），概率越高就容易选中
    # p=每个在函数中的值/所有在函数中的总数，即对应个体被选中的概率，这里选出的是索引
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE,
                           replace=True, p=fitness_score / fitness_score.sum())
    # 返回对应索引的值
    return pop[idx]


def crosscover(parent, pop):
    # 繁衍，小于配对比例
    if np.random.rand() < CROSS_RATE:
        # 从种群中随机选出一个个体，这里允许自交。。。
        i_ = np.random.randint(0, POP_SIZE, size=1)
        # 随机选择01基因是否继续遗传
        cross_points = np.random.randint(0, 2, size=DNA_SIZE).astype(np.bool)
        # 根据选出的个体与指定个体进行交配，基因遗传方式根据cross_points来选择
        parent[cross_points] = pop[i_, cross_points]
    return parent


def mutate(child):
    # 变异
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            # 如果发生变异，把1变为0.
            child[point] = 1 if child[point] == 0 else 0
            # child[point] = 0 if child[point] == 1 else 1
    return child


# 以上都是遗传算法的主要代码，下面是动态可视化的代码


def simData():
    pop = np.random.randint(1, size=(POP_SIZE, DNA_SIZE))
    for _ in range(N_GENERATIONS):
        F_values = F(translateDNA(pop))

        i = np.argmax(F_values)
        max_x = translateDNA(pop)[i]

        fitness_score = get_fitness(F_values)
        pop = select(pop, fitness_score)
        pop_copy = pop.copy()

        for parent in pop:
            child = crosscover(parent, pop_copy)
            child = mutate(child)
            parent[:] = child
        # 将需要可视化的点x，y值传递给另一个函数
        yield max_x, F(max_x)


def convert_gif():
    # 第二种可视化方式
    import imageio

    fig = plt.figure()
    axes1 = fig.add_subplot(111)

    # 动态展示的函数
    plt.ion()
    x = np.linspace(*X_BOUND, 200)
    plt.plot(x, F(x))

    # 第一代种群个体
    pop = np.random.randint(1, size=(POP_SIZE, DNA_SIZE))
    frames = []
    for _ in range(N_GENERATIONS):
        # 将种群每个个体放入函数中
        F_values = F(translateDNA(pop))

        i = np.argmax(F_values)
        max_x = translateDNA(pop)[i]

        print(max_x)
        plt.plot(max_x, F(max_x), ".", color='blue')
        # 进行比较之后的值
        fitness_score = get_fitness(F_values)

        # 筛选，选出优质下一代
        pop = select(pop, fitness_score)

        pop_copy = pop.copy()

        # 每个个体进行交配
        for parent in pop:
            # 将当前选中的个体与种群中其他个体进行交配
            child = crosscover(parent, pop_copy)
            # 交配完的个体可能产生变异
            child = mutate(child)
            # 新个体取代原来的父/母
            parent[:] = child
        plt.pause(0.1)
        # 首先保存每次迭代的图片
        # plt.savefig("{}.png".format(_), format='png')
        # 将图片用这个函数进行读取（转换为array）
        # frames.append(imageio.imread("{}.png".format(_)))
    # 最后使用这个函数将所有的图片顺序合成一个gif图片，duration是间隔时间，单位是s
    # imageio.mimsave("imageio.gif", frames, 'GIF', duration=0.2)

    plt.ioff()
    plt.show()


def convert_mp4():

    # 绘制底板
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = np.linspace(*X_BOUND, 200)
    # 绘制函数图像
    plt.plot(x, F(x))

    # 绘制动态展示的控件——点
    line, = ax.plot([], [], 'bo', ms=10)

    def simPoints(simData):
        x, y = simData[0], simData[1]
        line.set_data(x, y)
        return line
    # 使用这个函数，fig是本身的画板，simPoints是需要绘制的点，simData是产生数据的函数传递给simPoints，interval动画间隔时间，单位是ms
    ani = animation.FuncAnimation(
        fig, simPoints, simData, interval=200)

    # 查看目前环境支持保存的格式。import matplotlib.animation as animation; animation.writers.list()

    # 一般不下载第三方工具，保存格式只有html
    # ani.save('animation.htm', dpi=70)

    # 使用命令conda install -c conda-forge ffmpeg进行下载安装
    # ani.save('animation.mp4', writer='ffmpeg')
    # 如果需要将html转换gif，推荐使用命令 ffmpeg -i animation.mp4 animation.gif
    plt.show()


if __name__ == '__main__':
    # 两种方式都可以转换为gif
    # convert_gif()
    convert_mp4()
