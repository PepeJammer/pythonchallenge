import requests, re
from bs4 import BeautifulSoup

def getParam(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser').prettify()
    param = "".join(re.findall('[0-9]', soup))
    if param == "16044":
        param = "8022"
    if param =="":
        print("Page found:"+soup)  
        exit()
    return param
def generateURL(param):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + param
    return url

i=0
parameter="12345"
while parameter!="":
    link = generateURL(parameter)
    parameter = getParam(link)
    i+=1
    print("Parameter:"+parameter)  
    print("Iteration:"+str(i))
