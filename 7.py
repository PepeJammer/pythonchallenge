from PIL import Image
from urllib.request import urlretrieve
import re

urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png", "oxygen.png")
img = Image.open("oxygen.png")
width = img.width
height = img.height
pixels=[]
for w in range(width):
    pixels.append(img.getpixel((w,height/2)))
pixels= pixels[::7]
values=[]
for r,g,b,a in pixels:
    values.append(r)
numbers = re.findall("[0-9]+", "".join(map(chr, values)))
for n in numbers:
    print(chr(int(n)))