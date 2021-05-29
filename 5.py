import pickle
from urllib.request import urlopen

data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
for l in data:
    print("".join([a*b for a,b in l]))