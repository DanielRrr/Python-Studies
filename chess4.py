import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if math.fabs(a - c) == math.fabs(b - c):
    print("YES")
else:
    print("NO")
