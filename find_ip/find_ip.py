# coding: utf-8

import re
from collections import Counter


if __name__ == '__main__':
    with open('/var/log/secure', 'r') as f:
        d = f.read()
    lst = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", d)
    lst = Counter(lst)
    lst = list(filter(lambda item: lst[item] > 3, lst))

    with open('/etc/hosts.deny', 'a') as f:
        for ip in lst:
            f.writelines(ip + '\n')
