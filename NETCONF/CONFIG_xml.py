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