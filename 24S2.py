string_list=[int(a) for a in input().split()]
output_list=['F']*int(string_list[0])
for string_num in range(int(string_list[0])):
    test_string=list(input())
    heavy_light_tracker=0
    for string_letter in test_string:
        if test_string.count(string_letter)>1:
            if heavy_light_tracker=="H":
                heavy_light_tracker=0
                break
            heavy_light_tracker="H"
        else:
            if heavy_light_tracker=="L":
                heavy_light_tracker=0
                break
            heavy_light_tracker="L"
    if heavy_light_tracker != 0:
        output_list[string_num]="T"
for item in output_list:
    print(item)