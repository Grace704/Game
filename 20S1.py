num=int(input())
y=-1
speed = [ [0]*2 for i in range(num)]
for i in range(num):
    val = input().split()
    speed[i][0] = int(val[0])
    speed[i][1] = int(val[1])
speed.sort()
for j in range(1,num):
    time_diff=speed[j][0]-speed[j-1][0]
    dis_diff=abs(speed[j][1]-speed[j-1][1])
    x=dis_diff/time_diff
    if x>y:
        y=x
print(y)
