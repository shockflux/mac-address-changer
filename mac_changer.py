#!/usr/bin/env python

import subprocess
import optparse
import re
def get_argument():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="enter interface to change it's mac address")
    parser.add_option("-m", "--mac", dest="mac_address", help="NEW MAC ADDRESS")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-]please specify an interface, use --help or -h for more info")
    elif not options.mac_address:
        parser.error("[-]please specify an mac address, use --help or -h for more info")
    return options


def mac_changer(interface,mac_address):
    print("[+] changing MAC ADDRESS of" + interface + "to new mac address" + mac_address)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search:
        return mac_address_search.group(0)
    else:
        print ("[-] could not find mac address")

options = get_argument()
current_mac=get_current_mac(options.interface)
print("CURRENT MAC="+str(current_mac))
mac_changer(options.interface , options.mac_address)
current_mac=get_current_mac(options.interface)
if(current_mac == options.mac_address):
    print("[+]MAC ADDRESS was successfully changed to "+current_mac)
else:
    print("[-]MAC ADDRESS was not changed")


