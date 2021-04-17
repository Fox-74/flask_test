import requests
a = requests.get('http://127.0.0.1:8080/rest')
print(a.json())