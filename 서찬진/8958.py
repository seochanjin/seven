a = int(input())
b=[]
for i in range(a):
    b.append(list(input()))

idx = 0
n=1
for i in range(a):
    for j in range(len(b[i])):
        if b[i][j] == 'O':
            idx += n
            n += 1
        else:
            n = 1

    print(idx)
    idx =0
    n=1