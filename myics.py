# coding: utf-8
import uuid
from datetime import datetime, timedelta, timezone
import time

import pandas as pd
from icalendar import Calendar, Event

tz_utc_8 = timezone(timedelta(hours=8))

time_dict = {
    1: [(8, 30), (9, 20)],
    2: [(9, 20), (10, 10)],
    3: [(10, 30), (11, 20)],
    4: [(11, 20), (12, 10)],
    5: [(13, 30), (14, 20)],
    6: [(14, 20), (15, 10)],
    7: [(15, 30), (16, 20)],
    8: [(16, 20), (17, 10)],
    9: [(18, 10), (19, 00)],
    10: [(19, 00), (19, 50)],
    11: [(20, 10), (21, 00)],
    12: [(21, 00), (21, 50)],
}
begin_year = 2020
begin_month = 9
begin_day = 7


def cread_event(lesson_name, classroom, teacher, start, end, freq=None):
    # 创建事件/日程
    event = Event()
    event.add('summary', lesson_name)

    dt_now = datetime.now(tz=tz_utc_8)
    event.add('dtstart', start)
    event.add('dtend', end)
    # 创建时间
    event.add('dtstamp', dt_now)
    event.add('LOCATION', classroom)
    event.add('DESCRIPTION', '教师：' + teacher)

    # UID保证唯一
    event['uid'] = str(uuid.uuid1()) + '/wnma3mz@gmail.com'
    if freq:
        event.add('rrule', freq)
    # event.add('priority', 5)
    return event


if __name__ == "__main__":

    cal = Calendar()
    cal.add('prodid', '-//JH-L//JH-L Calendar//')
    cal.add('version', '2.0')

    cls_lst = [
        {
            'name': 'nameA',
            'teacher': 'teacherA',
            'room': 'roomA',
            'time': [time_dict[1], time_dict[2]], # 第一节课-第二节课
            'week': [2, 3, 4, 5, 6, 7, 8, 9, 10], # 2-10周
            'day': [1, 3]   # 周一、周三
        },
        {
            'name': 'nameB',
            'teacher': 'teacherB',
            'room': 'roomB',
            'time': [time_dict[2], time_dict[4]],
            'week': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'day': [2]
        },
    ]

    begin_date = datetime(begin_year, begin_month, begin_day)
    for lesson in cls_lst:
        # 课程名字，教师，教室
        # 课程开始时间(s1小时，s2分钟)，课程结束时间(e1小时，e2分钟)
        # name, teacher, room = f'{lesson["name"]}-{lesson["room"]}', lesson['teacher'], lesson['room']
        name, teacher, room = lesson['name'], lesson['teacher'], lesson['room']
        s1, s2 = lesson['time'][0][0]
        e1, e2 = lesson['time'][-1][-1]
        for week in lesson['week']:
            # 第N周
            week_delta = timedelta(days=(week - 1) * 7)
            for day in lesson['day']:
                # 周N
                day_delta = timedelta(days=(day - 1))
                new_date = begin_date + week_delta + day_delta
                # 上课的年月日
                new_year, new_month, new_day = new_date.year, new_date.month, new_date.day
                ymd = [new_year, new_month, new_day]
                # 课程开始时间和结束时间
                start = datetime(*ymd, s1, s2, tzinfo=tz_utc_8)
                end = datetime(*ymd, e1, e2, tzinfo=tz_utc_8)

                cal.add_component(cread_event(name, room, teacher, start, end))

    with open('/data/ics_server/my.ics', 'wb') as f:
        f.write(cal.to_ical())
