
import urllib
import ssl
import json
from urllib.request import urlopen

api_key = 'AIzaSyBE9uTW092pQDZDkQ9KgRvwBMuVShiuM54'
url='https://maps.googleapis.com/maps/api/directions/json?origin=Paris&destination=Anto ny&mode=driving&key=AIzaSyBE9uTW092pQDZDkQ9KgRvwBMuVShiuM54'

url2="https://www.google.fr/"
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
json_obj=urllib.request.urlopen(url2,context=gcontext)
data=json.load(json_obj)


