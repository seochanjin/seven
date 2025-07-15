import sys

input = sys.stdin.readline

a = int(input())

n=[]

for i in range(a):
    n.append(int(input()))

n.sort()

sys.stdout.write('\n'.join(map(str, n)))
sys.stdout.write('\n')