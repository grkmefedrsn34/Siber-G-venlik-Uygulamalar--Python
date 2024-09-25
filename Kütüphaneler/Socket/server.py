import socket
import subprocess

host = '127.0.0.1'
port = 50001

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen()


conn,addr = server_socket.accept()

print("connected from : "+str(addr))

while True:
    data = conn.recv(1024).decode()
    print(data)
    result = subprocess.run(data,stdout=subprocess.PIPE,shell=True)
    response_data =result.stdout
    conn.send(response_data)
conn.close()