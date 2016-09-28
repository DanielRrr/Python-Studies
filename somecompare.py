s = str(input())
a = str(input())
b = str(input())
i = 0
while a in s:
    s = s.replace(a,b)
    if a in b:
      i = "Impossible"
    else: 
      i = i + 1
print(i)
