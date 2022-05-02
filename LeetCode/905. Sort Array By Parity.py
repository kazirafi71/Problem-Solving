lst = []
lst = list(map(int, input().split()))

new_list = []

new_list2=[]

for i in lst:
    if i % 2 == 0:
        new_list.append(i)
    else:
        new_list2.append(i)

print(new_list+new_list2)

