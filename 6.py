import re, zipfile

f = zipfile.ZipFile("channel.zip")
print(f.read("readme.txt").decode("utf-8"))
i="90052"
comments=[]
while True:
    param = f.read(i+".txt").decode("utf-8")
    comments.append(f.getinfo(i+".txt").comment.decode("utf-8"))
    match = re.search("([0-9]+)", param)
    if match == None:
        break
    i = match.group(1)
    print(param)
print("".join(comments))


