from ncclient import manager

ip = '12.0.0.145'
netconf_port = '830'
netconf_user = 'admin'
netconf_password = 'admin'

with manager.connect(host=ip,port=netconf_port,
                     username=netconf_user,
                     password=netconf_password,
                     hostkey_verify=False,
                     device_params={'name':'csr'},
                     allow_agent = False,
                     look_for_keys = False) as m:
    # c = m.get_config(source='running')
    # print(type(c))

     c = m.get_config(source='running').data_xml
   #  print(type(c))
   #  with open("D:\devnet\动手练习\{}.xml".format(ip),'w') as f:
   #      f.write(c)
    #      for capability in m.server_capabilities:
     #  print(capability)




