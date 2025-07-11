a, b = map(int, input().split())
c = list(map(int, input().split()))
d=[]

for i in range(a):
    if c[i] < b:
        d.append(c[i])

for i in range(len(d)):
    print(d[i], end=' ')
