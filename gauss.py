from cmath import sqrt, exp, pi

m = float(input())
s = float(input())
x = float(input())

z1 = 1.0 / (sqrt(2*pi)*s)
z2 = (x - m)/1.0/s
z2 = z2**2
z2 = (-0.5)*z2
z3 = z1*exp(z2)

print(z3)
