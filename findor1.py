n = int(input())
i = 1
if n == 1:
    print(1)
elif n != 1:
    while i < n:
        print(i*i)
        i = i+1
        if i*i > n:
           break
