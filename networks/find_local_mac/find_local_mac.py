# coding: utf-8
import os
import sys
import winreg
import requests
from pprint import pprint


def val2addr(val):
    addr = ""
    for ch in val:
        addr += ("%02x " % ord(ch))
    addr = addr.strip(" ").replace(" ", ":")[:17]
    return addr


def get_local_mac():
    net = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged'

    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, net)
    mac_addr = {}
    for i in range(50):
        try:
            guid = winreg.EnumKey(key, i)
            netKey = winreg.OpenKey(key, str(guid))
            (n, addr, t) = winreg.EnumValue(netKey, 5)
            (n, name, t) = winreg.EnumValue(netKey, 4)
            macAddr = val2addr(str(addr))
            netName = str(name)
            print('[+] ' + netName + ' ' + macAddr)
            mac_addr[netName] = macAddr
            winreg.CloseKey(netKey)
        except:
            continue
    return mac_addr


if __name__ == '__main__':
    s = requests.session()

    basic_url = 'https://api.wigle.net/api/v2/profile/user'
    headers = {
        "accept": "application/json",
    }
    s.auth = (username, password)
    t = s.get(basic_url)

    mac_addr = get_local_mac()

    url = 'https://api.wigle.net/api/v2/network/comment'

    headers["Content-Type"] = "application/x-www-form-urlencoded"
    for name, addr in mac_addr.items():
        data = {
            'netid': addr,
            'comment': name,
        }
        print(data)
        res = s.post(url, data=data, headers=headers)
        pprint(res.json())
