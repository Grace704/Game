num1=list(input())
num2=list(input())
s=""
q=""
if len(num1)==len(num2):
    for i in range(len(num1)):
        if num1[i]!=num2[i]:
            s=str(num1[i])+" "+str(num2[i])
            q="-"
else:
    for j in range (len(num1)):
        if num1[j]!=num2[j]:
            q=num1[j]
            num1.remove(num1[j])
        elif len(num1)==len(num2):
            for i in range (len(num1)):
                if num1[i]!=num2[i]:
                    s=str(num1[i])+" "+str(num2[i])

print(s)
print(q)
    