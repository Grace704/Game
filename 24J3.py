people=int(input())
a=0
b=0
c=0
num=0
f=[]
for j in range (people):
    f.append(input())
f.sort(reverse=True)
a=int(f[0])
for i in range(people):
    if a>int(f[i]) and b<int(f[i]):
        b=int(f[i])
    elif a>int(f[i]) and b>int(f[i]) and c<int(f[i]):
        c=int(f[i])

for x in range(people):
    if int(f[x])==c:
        num+=1
print(str(c)+" "+str(num))