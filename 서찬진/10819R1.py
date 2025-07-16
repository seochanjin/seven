import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

m_s = 0

def solve(l):
    max_sum=0
    for i in range(len(l)-1):
        max_sum+=abs(l[i]-l[i+1])
    return max_sum


for i in permutations(a):
    m_s = max(solve(i), m_s)

print(m_s)