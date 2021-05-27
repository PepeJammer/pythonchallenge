import sys
i=0
letters= []
cipher=[]
letters_offset= []

print("Enter text:")
text = ""
try:
    text = str(input())
except: 
    print("Enter valid text")
    sys.exit()
print("Enter offset 1-25:")
o=0
try:
    o=int(input())
    if o>25 or o<1:
        sys.exit()
except: 
    print("Enter valid offset")
    sys.exit()
    
alphabet="abcdefghijklmnopqrstuvwxyz" 
for c in alphabet:
    letters.append(c)
letters_offset1=letters.copy()
letters_offset2=letters.copy()     
print("Alphabet:", letters)
for l in letters_offset1:
    if i+o>25:
        letters_offset1[i]=letters_offset2[abs(26-i-o)]
    if i+o<=25:
        letters_offset1[i]=letters_offset1[i+o]
    i+=1
print("Alphabet with offset:", letters_offset1)

for c in text:
    cipher.append(c)
y=0
z=0
encoded=""
for c in cipher:
    while y!=len(cipher):
        if cipher[y]==letters[z]:
            encoded=encoded+letters_offset1[z]
            y+=1
            z=-1
        elif z==25:
            encoded=encoded+cipher[y]
            y+=1
            z=-1
        z+=1

print("Decoded text:" + encoded)
    


                
