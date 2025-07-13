a = int(input())

b = list(map(int, input().split()))
idx = a

for i in range(a):
    if b[i] == 1:
        idx -= 1
        continue
    for j in range(2, b[i]):
        if b[i] % j == 0:
            idx-=1
            break

print(idx)





