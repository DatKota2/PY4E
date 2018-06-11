import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = int(input('Enter count: '))
print('Count = ', count)
position = int((input('Enter position: '))) - 1
print('Position =', position)

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    tagList = list()
    for tag in tags:
        tagList.append(tag)
    url = tagList[position]
    tagList = list()
