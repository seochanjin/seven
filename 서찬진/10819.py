import sys

input = sys.stdin.readline

a=int(input())
b=list(map(int, input().split()))

max_result = 0

def calculate(l):
    total = 0
    for i in range(len(l)-1):
        total += abs(l[i]-l[i+1])
    return total


def whatthe(depth):
    global max_result
    if depth == a:
        max_result = max(max_result, calculate(b))
        return
    
    for i in range(depth, a):
        b[depth], b[i] = b[i], b[depth]
        
        whatthe(depth+1)
        
        b[depth], b[i] = b[i], b[depth]

whatthe(0)
print(max_result)
