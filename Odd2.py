n = int(input())

xs = []

a = 1
h = 2
while (a <= n):
   xs.insert(0, a)
   a += h
print(sorted(xs))
