# coding: utf-8
import sys
import base64
import requests
import json

import sys
import time
import keyboard
from PIL import ImageGrab, Image

"""
keybord与ImageGrab作为客户端截图
api.mathpix作为识别api，需要mathpix的appkey
"""

url = "https://api.mathpix.com/v3/latex"
headers = {"app_id": "trial", "Content-type": "application/json"}


def img2latex(file_path='tmp.png'):
    # 将文件路径放在此处
    with open(file_path, "rb") as f:
        data = f.read()
    image_uri = "data:image/jpg;base64," + base64.b64encode(data).decode()
    # id:             32位长度
    # token:          32位长度
    # detaul_app_key: 32位长度
    # app_key         32位长度
    headers["app_key"] = app_key
    r = requests.post(url,
                      data=json.dumps({'url': image_uri}),
                      headers=headers)

    return json.loads(r.text)["latex"]


def screen(file_path):
    keyboard.wait(hotkey='ctrl+alt+a')
    keyboard.wait(hotkey='enter')
    # keyboard.wait(hotkey='windows+shift+s')
    time.sleep(0.5)

    im = ImageGrab.grabclipboard()
    im.save(file_path)


if __name__ == "__main__":

    file_path = '100009e256.png'
    formula = img2latex(file_path=file_path)
    print(formula)
    # while 1:
    #     screen(file_path)
    #     formula = img2latex(file_path=file_path)
    #     print(formula)

