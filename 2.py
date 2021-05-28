from urllib.request import urlopen
import re

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
text = urlopen(url).read().decode()
symbols = re.findall("<!--(.*?)-->", text, re.DOTALL)[-1]
chars={}
for c in symbols:
    if c in chars:
        chars[c]+=1
    else:
        chars[c]=1
print(chars) 
