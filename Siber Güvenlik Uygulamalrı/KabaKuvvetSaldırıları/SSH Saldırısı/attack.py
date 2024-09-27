import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip ="10.10.10.128"
port = 22
username = "msfadmin"
password = "msfadmin"

ssh.connect(ip,port=port,username=username,password=password)

command = 'cat/etc/passwd'

stdin , stdout , stderr = ssh.exec_command(command)

cmd_output = stdout.read()
ssh.close()

#print(cmd_output)

etc_passwd = cmd_output.decode().split("\r")

userList = []

for ep in etc_passwd:
    if "/bin/bash" in ep or "/bin/sh" in ep:
        #print(ep)
        user = ep.split(":")[0]
        userList.append(user)
print(userList)

