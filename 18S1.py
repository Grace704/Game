n=int(input())
v=[]
for i in range(n):
    v.append(int(input()))
v.sort()
ans=float("inf")
for i in range(1,n-1):
    left = (v[i] +v[i-1])/2
    right = (v[i] + v[i+1])/2
    ans = min(ans, right-left)
print(ans)