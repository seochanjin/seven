t = int(input())
a = []
b = []
c = []
for i in range(t):
    a.append(int(input()))
count = 0


def search_prime_number(arg):
    for x in arg:
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
        b.append(c)


def all_add(arg):
    global count
    all_line = []
    for i in range(len(arg) - 1):
        for x in range(i, len(arg)):
            if (arg[i] + arg[x]) == a[count]:
                all_line.append([arg[i], arg[x]])
    count += 1
    if len(all_line) <= 1:
        return all_line[0]
    else:
        index = minus(all_line)
        return all_line[index]


def minus(matrix):
    save = []
    for [a, b] in matrix:
        save.append(a - b)
    a = max(save)

    idx = save.index(a)
    return idx


def printf(matrix):
    for i in range(len(matrix)):
        print(matrix[i][0], matrix[i][1])


search_prime_number(a)
answer = list(map(all_add, b))
printf(answer)
