import paramiko
from device import device_list
'''
USER =device_list[0]['hostname']
PASS =device_list[0]['password']
IP = device_list[0]['ip_address']
PORT = 22
'''

USER='zhy'
PASS='Eccom@123'
IP= '12.0.0.129'
PORT = 22

def get_config():
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   # ssh.connect(hostname=IP,port=PORT,username=USER,passphrase=PASS)
    ssh.connect(hostname='10.1.3.1', port=22, username='admin', passphrase='admin')
    #stdin,stdout,stderr=ssh.exec_command('show run | include name')
    stdin,stdout,stderr= ssh.exec_command('en')
    result=stdout.read().decode()
    print(str(result,encoding='utf-8'))
   # result = str(result,encoding='utf-8')
    err = stderr.read()
    ssh.close()
    return result

a = get_config()