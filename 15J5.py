a=int(input())
b=int(input())
c=a-b
if c==0 or b==1 or c==1:
    print(1)
else:
    if c<=b:
        print(c+c-3)
    else:
        print(b+1)