# coding: utf-8
import requests
from bs4 import BeautifulSoup
import asyncio
import random
import jieba

s = requests.session()


async def get_name_lst(num):
    """
    异步获取非主流网名
    Parameters
    ----------
    num: int
        页码、

    Returns
    ----------
    list:
        30个非主流网名组成的列表
    """
    url = 'http://www.qwangming.com/wm/id/21/pn/{}.html'.format(num)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    lst = soup.find(class_='list').find_all('td')
    lst = list(map(lambda name: name.text.strip(), lst))
    return lst


async def get_main(loop):
    """
    异步获取非主流网名主函数
    Parameters
    ----------
    loop:
        异步的loop

    Returns
    ----------
    list:
        任务完成后的结果——列表中含有100个列表，每个列表中有30个网名
    """
    tasks = [
        loop.create_task(get_name_lst(num)) for num in range(100)
    ]

    await asyncio.wait(tasks)

    return tasks


def get_name_lst_map(num):
    """
    map获取非主流网名主函数
    Parameters
    ----------
    num:
        页码

    Returns
    ----------
    list:
        30个非主流网名组成的列表
    """
    url = 'http://www.qwangming.com/wm/id/21/pn/{}.html'.format(num)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    lst = soup.find(class_='list').find_all('td')
    lst = list(map(lambda name: name.text.strip(), lst))
    return lst


def save_csv(lst):
    """
    保存网名到csv，每个网名对应的标签label为1。
    Parameters
    ----------
    lst:
        爬虫获取到的数据

    Returns
    ----------
        None
    """
    # 碾平多维数组
    from itertools import chain
    name_lst = list(chain(*lst))
    # 去重
    name_set = set(name_lst)

    d = {'name': list(name_set), 'lable': list(
        1 for _ in range(len(name_set)))}

    df = pd.DataFrame(d)
    # 保存为csv，注意在windows下的编码，和去除默认的index
    df.to_csv('name.csv', encoding='utf_8_sig', index=None)


def filter_stop(name):
    """
    过滤停用词和一些不合法词
    Parameters
    ----------
    name:
        列表中的每个名字

    Returns
    ----------
    bool
    """
    if (len(name) == 1) or (name.isdigit()) or ('.' in name) or (name.islower()):
        return False
    return True


def filter_word(name):
    """
    筛选出名字长度为3的。
    Parameters
    ----------
    name:
        列表中的每个名字

    Returns
    ----------
    bool
    """
    if len(name) == 3:
        return True
    return False


def cut_poem_book():
    """
    使用诗经来取名
    Parameters
    ----------

    Returns
    ----------
    list, list:
        使用两种分词方法过滤后的名字列表
    """
    with open('诗经.txt', 'r') as f:
        data = f.readlines()
    dstring = ''.join(d for d in data)

    # 使用两种方法进行分词
    d1 = jieba.cut(dstring)
    d2 = jieba.cut_for_search(dstring)

    # 过滤不合法名字
    d1 = filter(filter_stop, d1)
    d2 = filter(filter_stop, d2)
    # 筛选符合设定长度的名字
    d1_2 = list(filter(filter_word, d1))
    d2_2 = list(filter(filter_word, d2))

    return d1_2, d2_2


def cut_gushici(dstring):
    """
    使用gushici的api来取名
    Parameters
    ----------

    Returns
    ----------
    list, list:
        使用两种分词方法过滤后的名字列表
    """
    # 基本同上
    d1 = jieba.cut(dstring)
    d2 = jieba.cut_for_search(dstring)

    d1 = filter(filter_stop, d1)
    d2 = filter(filter_stop, d2)

    d1_2 = list(filter(filter_word, d1))
    d2_2 = list(filter(filter_word, d2))

    return d1_2, d2_2


def get_gushici(num):
    """
    map获取古诗词内容
    Parameters
    ----------

    Returns
    ----------
    str:
        一句古诗词
    """
    url = 'https://api.gushi.ci/rensheng.txt'
    return requests.get(url).text


if __name__ == '__main__':

    # 在数据量大的情况下，async会快速map
    # 异步方法
    # loop=asyncio.get_event_loop()
    # tasks=loop.run_until_complete(get_main(loop))
    # lst=[task.result() for task in tasks]
    # loop.close()
    # map方法
    # res = list(map(get_name_lst_map, tuple(range(100))))

    # 获取诗经的名字
    d1_2, d2_2 = cut_poem_book()

    # map方法获取guchici中的句子
    texts = list(map(get_gushici, tuple(range(50))))
    st = ''.join(texts)

    d1_2, d2_2 = cut_gushici(st)

    # 选出十个不重复的名字
    wlst = random.sample(d1_2, 10)
