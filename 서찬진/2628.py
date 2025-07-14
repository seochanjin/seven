a = list(map(int, input().split()))
b = int(input())

g = [0,a[0]]
s = [0,a[1]]

for i in range(b):
    d, v = map(int, input().split())

    if d == 0:
        s.append(v)
    else:
        g.append(v)

g.sort()
s.sort()

max_g = 0
for i in range(1, len(g)):
    max_g = max(max_g, g[i]-g[i-1])

max_s=0
for i in range(1, len(s)):
    max_s = max(max_s, s[i]-s[i-1])

print(max_g*max_s)