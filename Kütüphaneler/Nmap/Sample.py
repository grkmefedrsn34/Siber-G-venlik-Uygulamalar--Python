import Nmap 

scanner = Nmap.PortScanner()

ip = '10.10.10.128'

scanner.scan(ip,'0-100','-sS')

#print(scanner.scaninfo())


print("host", ip, ":", scanner[ip].state())
