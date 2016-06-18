x = str(input())
i = x.find('f')
j = x.rfind('f')
if i == -1:
    print('No!')
elif i == j:
    print(i)
else:
    print(i, j)
