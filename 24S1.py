num_people=int(input())
hat_num=[]
for i in range (num_people):
    hat_num.append(int(input()))
people_seeing = 0
for hat_number in range(int(num_people/2)):
    if hat_num[hat_number]==hat_num[int(hat_number+num_people/2)]:
        people_seeing +=1
print(people_seeing*2)