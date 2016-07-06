s = input()
c = 0
for i in range(len(c)):
    if c[i].lower() == 'f':
        c += 1
        if c == 2: break
else:
    i = -1 if c else -2
 
print(i)
