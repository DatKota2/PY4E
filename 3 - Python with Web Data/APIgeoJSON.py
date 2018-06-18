import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location: ')
if len(address) < 1:
    address = 'South Federal University'

url = serviceurl + urllib.parse.urlencode(
    {'address': address})

print('Retrieving', url)
raw_json = urllib.request.urlopen(url)
data = raw_json.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    

place_id = js['results'][0]['place_id']
print("Place ID: {}".format(place_id))