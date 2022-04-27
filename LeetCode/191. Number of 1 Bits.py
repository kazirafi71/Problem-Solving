n = int(input())


x = (bin(n))
y = x[2:]
cnt = 0
for i in range(0, len(y)):
    if y[i] == "1":
        cnt += 1
    else:
        pass

print(cnt)
