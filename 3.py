from urllib.request import urlopen
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
text = urlopen(url).read().decode()
match = re.findall("[^A-Z][A-Z]{3}([a-z]){1}[A-Z]{3}[^A-Z]", text)

print(match) 
