# 配置csr-1loopback0ip地址
CONFIG0 = """
       <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <Loopback>
            <name>0</name>
            <description>ospf-RID</description>
            <ip>
              <address>
                <primary>
                  <address>1.1.1.1</address>
                  <mask>255.255.255.255</mask>
                </primary>
              </address>
            </ip>
          </Loopback>
        </interface>
      </native>
    </config>
"""
# 配置csr-2loopback0ip地址
CONFIG1 = """
       <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <Loopback>
            <name>0</name>
            <description>ospf-RID</description>
            <ip>
              <address>
                <primary>
                  <address>2.2.2.2</address>
                  <mask>255.255.255.255</mask>
                </primary>
              </address>
            </ip>
          </Loopback>
        </interface>
      </native>
    </config>
"""
#csr-1配置ospf
CONFIG2 = """ <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
          <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
            <id>1</id>
            <router-id>1.1.1.1</router-id>
          </ospf>
        </router>
      </native>
    </config>
"""
#csr-2配置ospf
CONFIG3 = """ <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
          <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
            <id>1</id>
            <router-id>2.2.2.2</router-id>
          </ospf>
        </router>
      </native>
    </config>
"""
# 配置G1和L1的ospf
CONFIG4 = """     <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <GigabitEthernet>
            <name>1</name>
            <ip>
              <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                <process-id>
                  <id>1</id>
                  <area>0</area>
                </process-id>
                <network>point-to-point</network>
              </ospf>
            </ip>
          </GigabitEthernet>
          <Loopback>
            <name>0</name>
            <ip>
              <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                <process-id>
                  <id>1</id>
                  <area>0</area>
                </process-id>
                <network>point-to-point</network>
              </ospf>
            </ip>
          </Loopback>
        </interface>
      </native>
    </config>
"""
