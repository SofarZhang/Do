from ping3 import ping


def ping_host(ip):
    """
    获取节点的延迟的作用
    :param node:
    :return:
    """
    ip_address = ip
    response = ping(ip_address)
    print(response)
    if response is not None:
        delay = int(response * 1000)
        print(delay, "延迟")
        # 下面两行新增的


ping_host('www.baidu.com')