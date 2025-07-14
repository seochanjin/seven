a = input()
idx = 0

if int(a) < 100:
    print(int(a))

else:
    for i in range(100, int(a)+1):
         b=str(i)
         if int(b[0])-int(b[1]) == int(b[1])-int(b[2]):
            idx+=1




    result = idx+99      
    print(result)

