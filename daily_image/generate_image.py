# coding: utf-8
# generate_image.py
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
import datetime
from lunar import Lunar
import requests


def get_weekday():
    date = datetime.datetime.now()
    d = {
        '0': u'周日',
        '1': u'周一',
        '2': u'周二',
        '3': u'周三',
        '4': u'周四',
        '5': u'周五',
        '6': u'周六',
    }
    return d[str(date.weekday())]


def draw_rectangle(x1, y1, x2, y2, size):
    # 左上角点与右上角点
    draw.line((x1, y1, x2, y1), fill=color, width=size)
    draw.line((x1, y2, x2, y2), fill=color, width=size)
    draw.line((x1, y1, x1, y2), fill=color, width=size)
    draw.line((x2, y1, x2, y2), fill=color, width=size)


def text_words(font_style, font_size, x, y, word, encoding="unic"):
    font = ImageFont.truetype(font_style, font_size, encoding=encoding)  # 设置字体
    draw.text((x, y), word, color, font)


def get_center_x(word_num, font_size):
    return (w - font_size * word_num) / 2


def add_date_words():
    # 日期
    today = time.strftime("%Y.%m.%d")
    # 周几
    weekday = get_weekday()
    # 几号
    num = str(int(today.split('.')[-1]))
    # 农历
    # ct = datetime.datetime(2015,2,19,13,0,15)
    # ln = Lunar(ct)
    # print('公历 {}  北京时间 {}'.format(ln.localtime.date(), ln.localtime.time()))
    # print('{} 【{}】 {}年 {}日 {}时'.format(ln.ln_date_str(), ln.gz_year(), ln.sx_year(), ln.gz_day(), ln.gz_hour()))
    # print('节气：{}'.format(ln.ln_jie()))
    ln = Lunar()
    lc_day = ln.gz_year() + '年' + ' ' + ln.ln_date_str()[2:]
    # 已过多少天
    d1 = datetime.datetime.strptime('2018.01.01', '%Y.%m.%d')
    d2 = datetime.datetime.strptime(today, "%Y.%m.%d")
    delta = (d1 - d2).days
    percent = round(-delta / 365 * 100, 2)
    delta_days = '第{}天，进度已消耗{}%'.format(-delta, percent)

    font_size = 40
    text_words(font_style, font_size, 40, 40, today)
    text_words(font_style, font_size, w -
               font_size * 2 - 40, 40, weekday)  # 两个字符

    font_size = 130
    temp_height = h * (1 - 0.618) - font_size
    temp_x = get_center_x(1, font_size)
    text_words(font_style, font_size, temp_x,
               temp_height, num)

    temp_height += font_size
    font_size = 20
    temp_x = get_center_x(7.5, font_size)
    text_words(font_style, font_size, temp_x,
               temp_height + 10, lc_day)  # 7.5字符
    temp_x = get_center_x(11 + len(str(delta)) * 0.5 - 0.5, font_size)
    text_words(font_style, font_size, temp_x, temp_height +
               font_size + 15, delta_days)  # 11 + 0.5/1/1.5字符

    # 进度条
    draw.rectangle((40, 400, w - 40, 440), 'darkgray', 'darkgray')
    draw.rectangle((40, 400, (w - 40 * 2) * percent *
                    0.01 + 40, 440), color, color)

    gushi = requests.get('https://api.gushi.ci/all.json')

    try:
        data = gushi.json()
        title = data['origin']
        author = data['author']
        content = data['content']
        temp_x = get_center_x(len(title), font_size)
        text_words(font_style, font_size, temp_x,
                   (h - 40 - 500) * 0.2 + 500, title)
        temp_x = get_center_x(len(content), font_size + 2)
        text_words(font_style, font_size + 5, temp_x, 600, content)
        text_words(font_style, font_size, w - (len(author) + 2 + 1)
                   * font_size - 40, 700, '——' + author)
    except:
        print('获取古诗词失败')


if __name__ == '__main__':
    w, h = 600, 800
    color = "deepskyblue"
    font_style = "kaiti.ttf"

    array = np.ndarray((h, w, 3), np.uint8)
    array[:, :, 0] = 255
    array[:, :, 1] = 255
    array[:, :, 2] = 255
    global draw

    image = Image.fromarray(array)
    # 创建绘制对象
    draw = ImageDraw.Draw(image)

    # 外围边框
    draw_rectangle(0, 0, w, h, 8)
    # 外围第二个边框
    draw_rectangle(15, 15, w - 15, h - 15, 3)
    # 内部边框
    draw.rectangle((40, 500, w - 40, h - 40), 'white', color)

    add_date_words()
    image.save(str(time.time())[:11] + 'png')
    # return image
    # image.show()
    # image.save('test.png')
