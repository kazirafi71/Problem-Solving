n = int(input())
while n > 0:
    n = n-1
    lst = []
    lst = list(map(int, input().split()))
    a = lst[0]
    b = lst[1]
    if a == 0:
        print(1)
    elif a!= 0 and b==0:
        print(a+1)
    elif a!= 0 and b!=0:
        print(a+1+b*2)
