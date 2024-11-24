num=int(input())
num1=input().split()
num2=input().split()
a=0
for i in range(0,num):
    a+=int(num2[i])*min(int(num1[i]),int(num1[i+1]))
    a+=abs(int(num1[i+1])-int(num1[i]))*int(num2[i])/2
if a%1==0:
    print(int(a))
else:
    print(a)