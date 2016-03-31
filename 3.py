X = int(input())
H = int(input())
M = int(input())
C = X // 60 + H + (X % 60 + M)//60 % 24
print(C)
print((X % 60 + M) % 60)
