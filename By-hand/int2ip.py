# 引用正则来三等分字符串
import re

# 转换成二进制数
bi = "{0:b}".format(3405803777)
# 补齐32位
bi = "0"*(32-len(bi))+bi
# 8个一组算出每8个数字的十进制，然后再加“，”分隔
ret_ip_string = '.'.join(list(map(lambda x:str(int(x,2)),re.findall(r'.{8}',bi))))
# 打印ip字符串
print(ret_ip_string)