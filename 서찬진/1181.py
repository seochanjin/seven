import sys

input = sys.stdin.readline
write = sys.stdout.write

a = int(input())

b=[]

for i in range(a):
    b.append(input().rstrip())

b=list(set(b))



b.sort(key=lambda x: (len(x),x) )


for i in range(len(b)):
    write(b[i] + '\n')
