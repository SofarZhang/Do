CONFIG0 = """
       <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <Loopback>
            <name>111</name>
            <description>111-test</description>
            <ip>
              <address>
                <primary>
                  <address>77.77.77.77</address>
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
            <name>111</name>
            <description>111-test</description>
            <ip>
              <address>
                <primary>
                  <address>88.88.88.88</address>
                  <mask>255.255.255.255</mask>
                </primary>
              </address>
            </ip>
          </Loopback>
        </interface>
      </native>
    </config>
"""