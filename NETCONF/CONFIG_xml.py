CONFIG0 = """
    <config>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
          <Loopback>
            <name>104</name>
            <description>loopback1-test</description>
            <ip>
              <address>
                <primary>
                  <address>44.44.44.44</address>
                  <mask>255.255.255.255</mask>
                </primary>
              </address>
            </ip>
          </Loopback>
        </interface>
      </native>
    </config>
"""