import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Sample: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual: http://py4e-data.dr-chuck.net/comments_90959.xml (Sum ends with 23)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

xml = urllib.request.urlopen(url, context=ctx).read()
print(xml)

data = ET.fromstring(xml)
print(data)

counts = data.findall('comments/comment/count')
print(counts)
for item in counts:
    print("Count:", item.find('count').text)
