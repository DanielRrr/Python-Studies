s = input()
print(s[1])
print(s[-2])
print(s[0:5:1])
print(s[0:len(s)-2:1])
for i in range(-1,len(s)):
    if i % 2 == 0:
        print(s[i], end='')
print()
for i in range(0,len(s)):
    if i % 2 != 0:
        print(s[i], end='',)
print()
print(s[::-1])
a = s[::-1]
for i in range(-1, len(a)):
    if i % 2 == 0:
        print(a[i], end='')
print()
print(len(s))
