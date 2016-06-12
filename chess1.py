a = int(input())
b = int(input())
c = int(input())
d = int(input())
s1 = a + b
s2 = c + d
if s1 % 2 == 0:
    b = (s2 % 2 == 0)
elif s1 % 2 != 0:
    b = (s2 % 2 != 0)
if b:
    print("YES")
else:
    print("NO")
