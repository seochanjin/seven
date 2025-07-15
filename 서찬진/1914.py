a = int(input())

def hanoi(a, x, y):

    if a>1:
        hanoi(a-1, x, 6-x-y)

    print(x,y)

    if a>1:
        hanoi(a-1, 6-x-y, y)


if a>20:
    print(2**a-1)
    
else:
    print(2**a-1)
    hanoi(a, 1, 3)




