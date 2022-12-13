from pysnmp.hlapi import *

ip = "192.168.88.1"

def main():

    oid_dict = { "Model": ("SNMPv2-MIB::sysDescr.0", "1.3.6.1.2.1.1.1.0"),
                "Uptime": ("SNMPv2-MIB::sysUpTime.0", "1.3.6.1.2.1.1.3.0"),
                "Interface count": ("SNMPv2-SMI::mib-2.2.1.0", "1.3.6.1.2.1.2.1.0")}
    
errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget((ip, 161)),
    ContextData(),
    ObjectType(ObjectIdentity("1.3.6.1.2.1.1.1.0"))
    )
)

for var in varBinds:
    print (var)

if __name__ == '__main__':
    main()