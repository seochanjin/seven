a=int(input())
b=int(input())

c=a*(b%10)
d=a*int((b%100)/10)
e=a*(int(b/100))

print(c)
print(d)
print(e)
print(a*b)