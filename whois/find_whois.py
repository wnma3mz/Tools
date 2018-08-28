# coding: utf-8
import pythonwhois
import urllib3
import time
import os
import datetime
import json

# 解释datetime类
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':

    with open('domains.txt', 'r') as f:
        d = f.readlines()
    shuffix_lst = [
        '.com.cn', '.edu.cn', '.jx.cn', '.com', '.cn', '.net', '.org',
        '.gov.cn', '.com', '.la', '.io', '.co', '.info', '.net', '.org', '.me',
        '.mobi', '.us', '.biz', '.xxx', '.ca', '.co.jp', '.net.cn', '.org.cn',
        '.mx', '.tv', '.ws', '.ag', '.com.ag', '.net.ag', '.org.ag', '.am',
        '.asia', '.at', '.be', '.com.br', '.net.br', '.bz', '.com.bz',
        '.net.bz', '.cc', '.com.co', '.net.co', '.nom.co', '.de', '.es',
        '.com.es', '.nom.es', '.org.es', '.eu', '.fm', '.fr', '.gs', '.in',
        '.co.in', '.firm.in', '.gen.in', '.ind.in', '.net.in', '.org.in',
        '.it', '.jobs', '.jp', '.ms', '.com.mx', '.nl', '.nu', '.co.nz',
        '.net.nz', '.org.nz', '.se', '.tc', '.tk', '.tw', '.com.tw', '.idv.tw',
        '.org.tw', '.hk', '.co.uk', '.me.uk', '.org.uk', '.vg'
    ]
    # 保证先匹配有两个后缀的域名
    sorted(shuffix_lst, key=len)[::-1]
    # 获取当前时间用于建立文件夹
    time_stamp = str(time.time())[:10]
    os.mkdir('domains_{}'.format(time_stamp))
    for line in d:
        name, url = line.split()
        # 解析主机名
        url = urllib3.get_host(url)[1]
        # 获取主站
        for shuffix in shuffix_lst:
            if shuffix in url:
                url = url.split(shuffix)[0].split('.')[-1] + shuffix
                break
        print(url)

        try:
            res = pythonwhois.get_whois(url)
        except:
            res = '{}: 解析失败'.format(url)
        with open('domains_{}/{}-{}.txt'.format(time_stamp, name, url),
                  'w') as f:
            json.dump(res, f, ensure_ascii=False, cls=DateEncoder, indent=4)
