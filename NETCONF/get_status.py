#解释器版本：python3.8
# 学员：张海燕
# Github：Sofar_zhang

import ntpath
import re
from ncclient import manager
import xml.etree.ElementTree as ET
import  sys
import  ipaddress
from prettytable import PrettyTable

import time
current_time = time.asctime( time.localtime(time.time()) )


print(current_time)

devicelist = [
    {'name':'csr1000v-1','ip':'10.1.1.171','netconf_port':'830','username':'admin','password':'admin',
     'params':'csr'},
    {'name':'csr1000v-2','ip':'10.1.1.182','netconf_port':'830','username':'admin','password':'admin',
     'params':'csr'}
]

get_status1="""
    <filter>
        <ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
            <ospfv2-instance>
                <ospfv2-area>
                    <ospfv2-interface>
                        <ospfv2-neighbor/>
                    </ospfv2-interface>
                </ospfv2-area>
            </ospfv2-instance>
        </ospf-oper-data>
    </filter>
"""


def netconf_connect(host_ip,params,
                    port=830,user='admin',password='admin'):
    x = manager.connect(host=host_ip,
                        port=port,
                        username=user,
                        password=password,
                        hostkey_verify=False,
                        device_params={'name':params},
                        allow_agent=False,
                        look_for_keys=False)
    return x


if __name__ == '__main__':
    for i in range(len(devicelist)):
        device_name = devicelist[i]['name']
        device_ip = devicelist[i]['ip']
        device_port = devicelist[i]['netconf_port']
        device_username = devicelist[i]['username']
        device_password = devicelist[i]['password']
        device_params = devicelist[i]['params']
        m = netconf_connect(device_ip,device_params,device_port,device_username,device_password)
        try:
            if device_name =='csr1000v-1':
                get_status = get_status1
                peer_rid_tag = '{http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper}nbr-id'
                peer_ip_tag = '{http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper}address'
                # print(type(get_status))
            elif device_name =='csr1000v-2':
                get_status = get_status1
                peer_rid_tag = '{http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper}nbr-id'
                peer_ip_tag = '{http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper}address'
                # print(type(get_status))
        except:
            print(1)

        # status = m.get(get_status)
        # print('='*80)
        # print(type(status))

        # status = m.get(get_status).data
        # print('=' * 80)
        # print(type(status))
        # print(status)

        status = m.get(get_status).data
        tag_text = status.findtext(".//" + peer_rid_tag)
        tag_text1 = status.findtext(".//" + peer_ip_tag)
        # print(type(status))
        # print(tag_text)

        if tag_text.find('.') == -1:
            RID = ipaddress.IPv4Address(int(tag_text))#IP10进制转换点分十进制
        else:
            RID = tag_text
        # print("RID:",RID)

        if tag_text1.find('.') == -1:
            RID1 = ipaddress.IPv4Address(int(tag_text))#IP10进制转换点分十进制
        else:
            RID1 = tag_text1
        # print("接口IP为：",RID)
        x = PrettyTable(field_names=["ip", "name", "RID", "neighbor_interface_address"])
        x.add_row([device_ip, device_name, RID, RID1])
        print(x)


        with open("{}_".format(device_ip) + current_time + ".txt","w") as f:
            f.write(str(x))



        # if tag_text.find('.') == -1:
        #     PEER_RID=ip10_to_ip(int(tag_text))
        # else:
        #     PEER_RID=tag_text
        # print(PEER_RID)

        #以当前元素为根的树迭代器
        # list=[]
        # for i in status.iter():
        #   print(i.tag)

        # print(list)











