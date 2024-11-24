import random
num_digits = int(input("How many digits do you want to have? "))
a=[]
f=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
j=['!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','|','[',']']
for i in range(num_digits):
    d=random.choice([1, 2, 3])
    if d==1:
        g=random.randint(0,25)
        a.append(str(f[g]))
    elif d==2:
        h=random.randint(0,20)
        a.append(str(j[h]))
    else:
        b=random.randint(0,9)
        a.append(str(b))
c=" ".join(a)
print(c)
