a, b, c, d = map(int, input().split())

distances = [a, b, c - a, d - b]

print(min(distances))
