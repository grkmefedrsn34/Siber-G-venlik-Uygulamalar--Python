from scapy.all import *

def sniffPckt(pkt):
    pkt.show()

# Sadece TCP paketlerini dinlemek için:
#sniff(prn=lambda x: x.summary(), timeout=5, iface="eth0", filter="tcp")
scapy_sniff = sniff(prn=sniffPckt, timeout=5, iface="eth0",stop_filter = lambda x:x.haslayer(ICMP))

wrcap('btkakademi.pcap',scapy_sniff)


#Eğer doğru ağ arayüzü seçilmişse ve dinlemek istediğiniz süreyi ayarladıysanız, bu kod 5 saniye boyunca tüm ağ trafiğini özetleyerek ekrana yazdıracaktır.