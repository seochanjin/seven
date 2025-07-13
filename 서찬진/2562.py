a=[]
for i in range(9):
    a.append(int(input()))

max = a[0]
idx = 1

for i in range(9):
    if a[i] > max:
        max = a[i]
        idx = i+1


print(max)
print(idx)