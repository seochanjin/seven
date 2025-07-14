a, b, v = map(int, input().split())

day = a - b
v = v - a

c = v / day + 1

print(c)
