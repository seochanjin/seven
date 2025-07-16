N = int(input())
path = [0] * N
visited = [False] * N
visited_1 = [False] * (2 * N -1)
visited_2 = [False] * (2 * N -1)
count = 0
def queen(depth):
    global count
    if depth == N:
        count += 1
        return
    
    for j in range(N):
        if not visited[j] and not visited_1[depth+j] and not visited_2[depth-j+N-1]:
            visited[j] = visited_1[depth+j] =  visited_2[depth-j+N-1] = True
            path[depth] = j
            queen(depth + 1)
            visited[j] = visited_1[depth+j] =  visited_2[depth-j+N-1] = False
            

queen(0)
print(count)
