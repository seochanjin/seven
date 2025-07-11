a=int(input())
b=[]
for i in range(a):
    b.append(list(map(int, input().split())))
    
for i in range(a):
    print(b[i][0]+b[i][1])


