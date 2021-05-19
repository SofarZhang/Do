#! /usr/bin/env python
import lxml.etree as et
from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError

payload = [
'''
<edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <target>
    <running/>
  </target>
  <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interface>
        <Loopback>
          <name>1</name>
          <description>loopback1-test</description>
          <ip>
            <address>
              <secondary>
                <address>2.2.2.2</address>
                <mask>255.255.255.255</mask>
                <secondary/>
              </secondary>
              <primary>
                <address>1.1.1.1</address>
                <mask>255.255.255.255</mask>
              </primary>
            </address>
          </ip>
          <ipv6>
            <address>
              <autoconfig>
                <default/>
              </autoconfig>
            </address>
            <mtu>9216</mtu>
          </ipv6>
        </Loopback>
      </interface>
    </native>
  </config>
</edit-config>
''',
]

if __name__ == '__main__':

    parser = ArgumentParser(description='Usage:')

    # script arguments
    parser.add_argument('-a', '--host', type=str, required=True,
                        help="Device IP address or Hostname")
    parser.add_argument('-u', '--username', type=str, required=True,
                        help="Device Username (netconf agent username)")
    parser.add_argument('-p', '--password', type=str, required=True,
                        help="Device Password (netconf agent password)")
    parser.add_argument('--port', type=int, default=830,
                        help="Netconf agent port")
    args = parser.parse_args()

    # connect to netconf agent
    with manager.connect(host=args.host,
                         port=args.port,
                         username=args.username,
                         password=args.password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        # execute netconf operation
        for rpc in payload:
            try:
                response = m.dispatch(et.fromstring(rpc))
                data = response.data_ele
            except RPCError as e:
                data = e._raw

            # beautify output
            print(et.tostring(data, encoding='unicode', pretty_print=True))
