a = int(input())
b = int(input())
c = int(input())
if a < b and b < c:
    print(a)
elif a < b and b > c:
    if a < c:
        print(a)
    elif a > c:
        print(c)
elif a > b and b > c:
    print(c)
elif a > b and b < c:
    print(b)
elif a == b and a < c:
    print(a)
elif a == b and a > c:
    print(c)
elif b == c and a < b:
    print(a)
