import random
import subprocess
import re


charList = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

newMac = ""
for i  in range(12):
    newMac=newMac+random.choice(charList)
print(newMac)

ifConfigResult = subprocess.check_output("ifConfig eth0",shell=True).decode()
print(ifConfigResult)

oldMac = re.search("ether (.+)",ifConfigResult).group(). split(" ")
print(oldMac)


oldMac = re.search("ether(.*?)txqueuelen",ifConfigResult).group().strip()
print(oldMac)

subprocess.check_output("ifConfig eth0 down ",shell=True)
subprocess.check_output("ifConfig eth0 hw ether "+newMac,shell=True)
subprocess.check_output("ifConfig eth0 up ",shell=True)

print("Old Mac :", oldMac)
print("New Mac : ", newMac)