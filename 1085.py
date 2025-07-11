a, b, c, d = map(int, input().split())

e = abs(c-a) #4
f = abs(d-b) #1

if a >= e: #6>=4
    g = e  #g=4
else:
    g = a

if b >= f: #2>=1
    h = f  #h=1
else:
    h = b

if g <= h: #
    print(g)
    
else:
    print(h)