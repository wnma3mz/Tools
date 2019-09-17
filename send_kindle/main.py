# coding: utf-8
import requests
url = "http://fivefilters.org/kindle-it/send.php"

params = {
    "context": "send",
    "url": url_send, # 需要发送的网址链接
}

data = {
    "email": email, # kindle的邮箱，如123@kindle.cn，email=123
    "from": from_email, # 发送方的邮箱，前提是此邮箱允许发送
    "domain": "4",
    "save": "yes",
}

response = requests.post(url, params=params, data=data)
print(response.text)
if response.status_code == 200:
    print("success")
else:
    print("failed")