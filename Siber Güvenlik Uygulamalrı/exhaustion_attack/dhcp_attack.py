from scapy.all import * 

conf.checkIPaddr = False

ether,eth = Ether(dst="ff:ff:ff:ff:ff:ff") 
ip = IP(src="0.0.0.0",dst="255.255.255.255")

udp = UDP(sport=68,dport=67)
bootp = BOOTP(op=1,chaddr=RandMAC())
dhcp = DHCP(options=[("message-type","discover"),"end"])

dhcp_discover = eth/ip/udp/bootp/dhcp

ans,unans = srp(dhcp_discover,iface='eth0',verbose=False)

for p in ans:
    p[0].show()
    p[1].show()
    print(p[1].dst,":",p[1].yiaddr)
