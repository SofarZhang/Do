CONFIG0 = """<edit-config>
    <target>
      <running/>
    </target>
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
  </edit-config>
"""