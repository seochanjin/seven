import sys

input = sys.stdin.readline
write = sys.stdout.write

sum = 0
a=[]
for i in range(9):
    a.append(int(input()))
    sum = sum + a[i]

b = sum-100
c = []
idx_1 = 0
idx_2 = 0
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        
        if a[i]+a[j] == b:
            idx_1 = i
            idx_2 = j
            break
    if idx_1 != 0:
        break

if idx_1 > idx_2:
    del a[idx_1]
    del a[idx_2]

else:
    del a[idx_2]
    del a[idx_1]

a.sort()

for i in range(7):
    print(a[i])

