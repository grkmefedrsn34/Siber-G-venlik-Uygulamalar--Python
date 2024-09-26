import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = '10.10.10.128'

for port in range(1,65535):
    try:
       s.connect((ip,port))
       print(str(port),"open")
    except Exception as e:
        print(str(port),"closed")
    finally:
        pass