import requests
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf')

"""
输入微博图片的url可查询图片原创博主的个人信息
"""


def base62_encode(num):
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum = 0
    for ser, val in enumerate(num[::-1]):
        sum += (62 ** ser) * (alphabet.index(val))
    return sum

url = '//wx3.sinaimg.cn/thumb150/005QTOC5ly1fj7j8rwmdoj30ci0go75n.jpg'

old_uid = url.split('/')[-1][:8]

new_uid = int(old_uid, 16) if (old_uid[:3] != '005') and (old_uid[:3] != '006') else base62_encode(old_uid)

# print(new_uid)

user_url = 'https://m.weibo.cn/api/container/getIndex'

data = {
    # "uid":"2549228714",
    # "luicode":"10000011",
    # "lfid":"1076032549228714",
    # "featurecode":"20000320",
    "type": "uid",
    "value": str(new_uid),
    # "containerid":"1005052549228714",
}
s = requests.get(user_url, params=data)


from pprint import pprint

userinfo_json = s.json()['userInfo']
pprint(userinfo_json)

userinfo = {
    '名字:': userinfo_json['screen_name'],
    '简介:': userinfo_json['description'],
    '关注:': userinfo_json['follow_count'],
    '粉丝:': userinfo_json['followers_count'],
}

print(userinfo)
