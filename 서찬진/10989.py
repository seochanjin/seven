import sys

input = sys.stdin.readline
write = sys.stdout.write

a = int(input())
c = [0] * 10001

for i in range(a):
    n=int(input())
    c[n]+=1

for i in range(1, 10001):
    if c[i] > 0:
        for j in range(c[i]):
            write((f"{i}\n"))
