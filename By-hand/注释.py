import os
import sys

iplist = list()
ip = '192.168.1.11'
# ip = '172.24.186.191'
ip = 'www.baidu.com'
backinfo = os.system('ping -c 1 -w 1 %s' % ip)  # 实现pingIP地址的功能，-c1指发送报文一次，-w1指等待1秒
print
'backinfo'
print
backinfo
print
type(backinfo)
if backinfo:
    print
    'no'
else:
    iplist.append(ip)
print
iplist
