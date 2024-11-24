o
rig=input().strip()
origList=[0]*26
final=input().strip()
finalList=[0]*26

def convert(x):
    return ord(x)-ord("a")
for let in orig:
    origList[convert(let)]+=1
ast = False
astCount=0
for let in final:
    if let=="*":
        ast = True
        astCount+=1
    else:
        finalList[convert(let)]+=1
diff=0
for i in range(26):
    if finalList[i]>origList[i]:
        print("N")
        exit(0)
    diff+=origList[i]-finalList[i]
if ast:
    if astCount==diff:
        print("A")
    else:
        print("N")
else:
    if diff==0:
        print("A")
    else:
        print("N")