import requests

headers = {'Accept': 'image/svg+xml'}
url = "http://myservice/api/v1/resources/house/rooms/id/1"
resp = requests.get(url,headers=headers,auth=("person2","super"),verify = False)
print (resp.status_code)
print (resp.text)
