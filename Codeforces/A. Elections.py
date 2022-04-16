n = int(input())


def maximum(best, other1, other2):

    print(max(0, max(other1, other2) + 1 - best))


while n > 0:
    n = n-1
    st = []
    lst = list(map(int, input().split()))
    a = lst[0]
    b = lst[1]
    c = lst[2]

    print(maximum(a, b, c), end=" ")
    print(maximum(b, a, c), end=" ")
    print(maximum(c, a, b))
