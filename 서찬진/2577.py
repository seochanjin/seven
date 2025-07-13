a = int(input())
b = int(input())
c = int(input())

d = a * b * c

e = str(d)
f = [0 for i in range(10)]

for i in range(10):
    for j in range(len(e)):
        if int(e[j])==i:
            f[i] += 1
    print(f[i])