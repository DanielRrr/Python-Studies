import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == c or b == d:
    print("YES")
elif math.fabs(a - c) == math.fabs(b - c):
    print("YES")
else:
    print("NO")
