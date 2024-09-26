from scapy.all import Ether, ARP, srp

# Ethernet paketi ve ARP paketi oluşturuyoruz
eth = Ether()
arp = ARP()

# Ethernet broadcast adresi
eth.dst = "ff:ff:ff:ff:ff:ff"

# ARP hedef IP adresini ayarlıyoruz (subnet içinde 10.10.10.1 - 10.10.10.254)
arp.pdst = "10.10.10.1/24"

# Ethernet ve ARP paketlerini birleştiriyoruz
bcPckt = eth/arp

# Paketi gönderiyoruz, cevaplanan ve cevaplanmayan paketleri alıyoruz
ans, unans = srp(bcPckt, timeout=5)

print("#" * 30)

# Cevaplanan paketleri işliyoruz
for snd, rcv in ans:
    rcv.show()  # Cevaplanan paketleri göster
    print(rcv.psrc, ":", rcv.src)  # Kaynak IP ve MAC adresini yazdırıyoruz
