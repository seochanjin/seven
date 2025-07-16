import sys

n, r, c = map(int, sys.stdin.readline().split())

result = 0

def wtf(n, x, y):
    global result
    if n == 0:
        return
    half = 2**(n-1)
    block_size=half*half

    if r<x+half and c<y+half:
        wtf(n-1, x, y)
    elif r<x+half and c>=y+half:
        result+=block_size
        wtf(n-1, x, y+half)
        
    elif r>=x+half and c<y+half:
        result+=2*block_size
        wtf(n-1, x+half, y)
    else:
        result+=3*block_size
        wtf(n-1, x+half, y+half)

wtf(n, 0, 0)

print(result)
        