from py_http_api import PyHttpApi


api = PyHttpApi('https://api.github.com')
resp = api.get()
print(resp)
