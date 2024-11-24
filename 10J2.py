a=int(input())
b=int(input())
c=int(input())
d=int(input())
s=int(input())
ast=0
bst=0
step=s
steps=s
while step!=0:
    for i in range(a):
        if step==0:
            a=0
            b=0
        else:    
            ast+=1
            step-=1
    for i in range(b):
        if step==0:
            a=0
            b=0
        else:
            ast-=1
            step-=1
while steps!=0:
    for i in range(c):
        if steps==0:
            c=0
            d=0
        else:
            bst+=1
            steps-=1
    for i in range(d):
        if steps==0:
            c=0
            d=0
        else:
            bst-=1
            steps-=1
if bst>ast:
    print("Byron")
elif ast>bst:
    print("Nikky")
else:
    print("Tied")