a = int(input())
b=[]

for i in range(a):
    b.append(list(map(int, input().split())))

add = 0
avg=[]
for i in range(a):
    for j in range(1, b[i][0]+1):
        add+= b[i][j]
    avg.append(add / b[i][0])
    add = 0

addd = 0
for i in range(a):
    for j in range(1, b[i][0]+1):
        if b[i][j] > avg[i]:
            addd += 1
    avgg = addd / b[i][0] * 100
    addd = 0
    print(f"{avgg:.3f}%")