import requests

url = 'https://github.com'
#url2 = 'https://github.com'
headers = {'user-agent':'btk-akademi/1.1.1'}
try:
    r = requests.get(url,headers=headers,allow_redirects=False,timeout=0.001)
    #print(r.status_code)
    #print(r2.status_code)
    #print(r.text)
    #print(r.headers)
    print(r.headers.get('Date'))
    pass
except Exception as e:
    print(e)
    pass


#r2 = requests.get(url2)



# status_code
# text
#headers