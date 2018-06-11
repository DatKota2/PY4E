import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Alvern.html'
count = int(input('Enter count: '))
index = int((input('Enter position: '))) - 1

while count >= 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    print("Retrieving:", url)

    tags = soup('a')
    tagList = list()
    for tag in tags:
        tag = str(tag)
        tag = re.findall('"(.+)"', tag)
        tagList.append(tag[0])
    url = tagList[index]
    tagList = list()
    count = count - 1
