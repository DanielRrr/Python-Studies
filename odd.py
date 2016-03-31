n = int(input())

xs = range(1, n+1, 2)
ys = [0.0]*len(xs)

for i in range(len(xs)):
    ys[i] = xs[i]
print(ys)
