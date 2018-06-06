import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# http://py4e-data.dr-chuck.net/comments_90957.html
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')

total = 0
count = 0
for tag in tags:
    tag = str(tag)
    tmp = re.findall('[0-9]+', tag)
    for num in tmp:
        num = int(num)
        total = total + num
        count = count + 1

print(total, count)