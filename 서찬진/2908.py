a=list(map(str, input().split()))


b=int((a[0][::-1]))
c=int((a[1][::-1]))

if b>c:
    print(b)

else:
    print(c)