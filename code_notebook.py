# coding: utf-8

# 正则表达式
import re
# 查询xx后的关键词
re.findall('\"xxx\":(.*?),', s)
# IP地址
 re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", d)


# sqlite3
import sqlite3
# 连接sqlite3并查询
with sqlite3.connect(dbpath) as conn:
    cursor = conn.cursor()
    cursor.execute(sql_command)
    topic_id_list = cursor.fetchall()
