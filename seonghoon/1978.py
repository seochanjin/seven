a = int(input())

b = list(map(int, input().split()))
count = 0

for x in b:
    for i in range(2, x + 1):
        if x % i == 0:
            if x == i:
                count += 1
            else:
                break

print(count)
