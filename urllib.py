import urllib.request
from http.client import responses

opener = urllib.request.build_opener()
responce = opener.open("http://httpbin.org/get")
print(responce.read())