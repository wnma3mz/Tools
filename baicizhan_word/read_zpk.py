# coding: utf8
import sqlite3
import re
import os
import pickle


def read_zpk(filename):
    # 参考https://github.com/TheWanderingCoel/Baicizhan_ZpkDecomplier/blob/master/Zpk_Decomplier.ipynb
    # 读取百词斩的zpk文件
    with open(filename, encoding='utf-8', errors='ignore') as f:
        s = f.read()

    topic_id = re.findall('\"topic_id\":(.*?),', s)
    topic_id = topic_id[0]
    word = re.findall('\"word\":\"(.*?)\"', s)
    accent = re.findall('\"accent\":\"(.*?)\"', s)
    mean_cn = re.findall('\"mean_cn\":\"(.*?)\"', s)
    mean_en = re.findall('\"mean_en\":\"(.*?)\"', s)
    sentence = re.findall('\"sentence\":(.*?),', s)

    def fnone(item): return item[0] if len(item) != 0 else 'None'

    word = fnone(word)
    accent = fnone(accent)
    mean_en = fnone(mean_en)
    mean_cn = fnone(mean_cn)
    sentence = fnone(sentence)

    return word, accent, mean_cn, mean_en, sentence


def get_topic_id_list(dbpath, err_num=3):
    # 按照错误频次降序排列
    # 获取错词
    sql_command = """
    SELECT
        {}.topic_id
    FROM
        {}
    WHERE
        {}.err_num >= {}
    ORDER BY
        {}.err_num DESC
    """.format(word_book, word_book, word_book, err_num, word_book)
    # 取得所有topic_id
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_command)
        topic_id_list = cursor.fetchall()

    return topic_id_list


if __name__ == '__main__':
    # baicizhantopicprolem.db 错词，ts_learn_offline_dotopic_sync_ids_{} 错词记录
    # baicizhantopic.db       单词书，如四六级单词、考研单词等
    # word_media.db           单词书中已背单词
    # lockdb.db               当天背单词的计划
    root_path = os.getcwd()
    dbpath = os.path.join(root_path, 'baicizhantopicproblem.db')
    word_book = 'ts_learn_offline_dotopic_sync_ids_13'
    zpack_dir_path = os.path.join(root_path, 'zpack', '13')

    # 获取错词的id
    topic_id_list = get_topic_id_list(dbpath, 3)

    # 对当前目录（百词斩的词库默认存放位置默认进行遍历搜索）
    for dir_ in os.listdir(zpack_dir_path):
        # 遍历每个子文件夹
        zpack_path = os.path.join(zpack_dir_path, dir_)
        word_zpk_lst = os.listdir(zpack_path)
        # 如果文件名中有符合的id，则换入
        for word_zpk in word_zpk_lst:
            topic_id = word_zpk.split('_')[1]
            if (int(topic_id), ) in topic_id_list:
                i = topic_id_list.index((int(topic_id), ))
                topic_id_list[i] = [topic_id, read_zpk(
                    os.path.join(zpack_path, word_zpk))]

    with open('topic_id_list.pkl', 'wb') as f:
        pickle.dumps(topic_id_list, f)
