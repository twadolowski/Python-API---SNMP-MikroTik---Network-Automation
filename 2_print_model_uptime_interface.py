from pysnmp.hlapi import *

ip = "192.168.88.1"

def get_data(router_ip, obj_set):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget((router_ip, 161)),
        ContextData(),
        *obj_set
        )
    )
    return varBinds

def main():

    oid_dict = { "Model": ("SNMPv2-MIB::sysDescr.0", "1.3.6.1.2.1.1.1.0"),
                "Uptime": ("SNMPv2-MIB::sysUpTime.0", "1.3.6.1.2.1.1.3.0"),
                "Interface count": ("SNMPv2-SMI::mib-2.2.1.0", "1.3.6.1.2.1.2.1.0")}
    
    obj_types = set()
    for key in oid_dict:
        obj_types.add(ObjectType(ObjectIdentity(oid_dict[key][1])))
    results = get_data(ip, obj_types)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()