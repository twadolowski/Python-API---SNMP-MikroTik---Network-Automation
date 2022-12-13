import fire
from pysnmp.hlapi import *


def reboot(host, community="public", port=161):
    """Reboot MikroTik router with SNMP"""
    errorIndication, errorStatus, errorIndex, varBinds = next(
        setCmd(
            SnmpEngine(),
            CommunityData(community, mpModel=0),
            UdpTransportTarget((host, port)),
            ContextData(),
            ObjectType(ObjectIdentity("1.3.6.1.4.1.14988.1.1.7.1.0"), OctetString("1")),
        )
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print(
            "%s at %s"
            % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or "?",)
        )
    else:
        for varBind in varBinds:
            print(" = ".join([x.prettyPrint() for x in varBind]))


if __name__ == "__main__":

    fire.Fire(reboot)