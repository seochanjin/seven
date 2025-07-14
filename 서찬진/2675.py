a = int(input())
b=[]

for i in range(a):
    b.append(input().split())
    b[i][0] = int(b[i][0])

for i in range(a):
        c = b[i][0]
        d = b[i][1]
        for e in d:
              print(e*c, end='')
        print()


