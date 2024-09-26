import socket



ip = '10.10.10.128'

for port in range(1,100):
    try:
       s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       s.timeout(6.0)
       s.connect((ip,port))
       response = s.recv(1024)
       print(str(port),": open : Banner",response.decode())
    except socket.timeout as t:
        if(port==80):
            httpMessage = "GET / HTTP/1.0\r\n\r\n"
            s.send(httpMessage.encode())
            httpRes = s.recv(1024)
            print(str(port),": open : Banner",response.decode())
        else:
            print(str(port),": use different metod")
    except Exception as e:
        #print(str(port),"closed")
        pass
    finally:
        s.close()
