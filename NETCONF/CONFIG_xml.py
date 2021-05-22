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
<?xml version="1.0" encoding="utf-8"?>
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="5">
  <edit-config>
    <target>
      <running/>
    </target>
    <config>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>Eth-Trunk1</name>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
          <ip:ipv4 xmlns:ip="urn:ietf:params:xml:ns:yang:ietf-ip">
            <ip:address nc:operation="create" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
              <ip:ip>192.168.2.1</ip:ip>
              <ip:prefix-length>24</ip:prefix-length>
            </ip:address>
          </ip:ipv4>
        </interface>
      </interfaces>
    </config>
  </edit-config>
</rpc>
"""