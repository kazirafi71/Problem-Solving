t = int(input())

while t > 0:
    m, n = map(int, input().split())
    t -= 1
    cnt = 0

    if n<m:
        temp=n
        n=m
        m=temp
    if m==1 and n>=3:
        print(-1)

    else:
        print(2*n-2-(n+m)%2)
        
