t = int(input())
inputA = []
prime_num = []
all_plus = []
for i in range(t):
    inputA.append(int(input()))
count = 0
for x in inputA:
    c = []
    for i in range(2, x):
        if i == 2 or i == 3:
            c.append(i)
        else:
            for y in range(2, i + 1):
                if i % y == 0:
                    if i == y:
                        c.append(i)
                    else:
                        break
    prime_num.append(c)
all_line = []
answer = []
for i in prime_num:
    temple = []
    for x in range(len(i) - 1):
        for y in range(x, len(i)):
            if (i[x] + i[y]) == inputA[count]:
                temple.append([i[x], i[y]])
    if len(temple) <= 1:
        all_line.append(temple[0])
        count += 1
    else:
        save = []
        for [a, b] in temple:
            save.append(a - b)
        a = max(save)

        idx = save.index(a)
        all_line.append(temple[idx])
        count += 1


for i in range(len(all_line)):
    print(all_line[i][0], all_line[i][1])
