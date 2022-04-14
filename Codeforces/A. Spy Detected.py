
n = int(input())
while n > 0:
    k = int(input())
    lst = []
    lst = list(map(int, input().split()))
    n = n-1

    for i in range(0, k-1):

        if lst[i] == lst[i+1]:
            continue
        elif lst[0] != lst[1] and lst[1] == lst[2]:
            print(1)
            break
        elif lst[0] != lst[1] and lst[1] != lst[2]:
            if i == 0:
                print(2)
                break
        else:
            print(i+2)
            break
