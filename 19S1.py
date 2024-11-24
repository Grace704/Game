v=0
h=0
flip=input()
for i in range (len(flip)):
    if flip[i]=="H":
        h+=1
    elif flip[i]=="V":
        v+=1
if h%2==1 and v%2==1:
    print("4 3")
    print("2 1")
elif h%2==1:
    print("2 1")
    print("4 3")
elif v%2==1:
    print("3 4")
    print("1 2")
else:
    print("1 2")
    print("3 4")