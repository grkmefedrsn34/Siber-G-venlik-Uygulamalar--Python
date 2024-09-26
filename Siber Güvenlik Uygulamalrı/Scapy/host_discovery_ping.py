from scapy.all import IP, ICMP, sr1

# IP ve ICMP paketlerini oluşturuyoruz
ip = IP()
icmp = ICMP()

# IP ve ICMP paketlerini birleştiriyoruz
pingPckt = ip/icmp

# IP adresi ön ekini tanımlıyoruz
addr = "10.10.10."
ipList = []

# 0'dan 255'e kadar tüm IP'lere ping atıyoruz
for i in range(256):
    # IP paketinin hedef adresini güncelliyoruz
    pingPckt[IP].dst = addr + str(i)
    print(pingPckt[IP].dst)

    # Paketi gönderip cevabı alıyoruz, timeout süresi 0.5 saniye
    response = sr1(pingPckt, timeout=0.5, verbose=False)

    # Eğer bir yanıt alırsak IP'nin aktif olduğunu söylüyoruz
    if response:
        print(pingPckt[IP].dst, "is up")
        ipList.append(pingPckt[IP].dst)
    else:
        pass

# Aktif IP adreslerini listeliyoruz
print(ipList)
