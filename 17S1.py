day=int(input())
s1=input().split()
s2=input().split()
v1=0
v2=0
x=0
for i in range(day):
    v1+=int(s1[i])
    v2+=int(s2[i])
    if v1==v2:
        x=i+1
print(x)
