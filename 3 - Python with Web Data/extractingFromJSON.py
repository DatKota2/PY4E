import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Sample: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual: http://py4e-data.dr-chuck.net/comments_90960.json (Sum ends with 92)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_90960.json'

print('Retreiving', url)

raw_json = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retreived {} characters.'.format(len(raw_json)))

data = json.loads(raw_json)
print('Count', len(data['comments']))

total = 0

for item in data['comments']:
    total = total + item['count']

print('Sum:', total)