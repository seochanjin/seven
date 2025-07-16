n=3
a=[2, 4, 6, ]
visited = [False]*n
lits = [0]*n
count =0

def solve(depth):
    global count
    if n == depth:
        count+=1
        print(lits)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            lits[depth] = a[i]
            solve(depth+1)
            visited[i] = False

solve(0)
print(count)