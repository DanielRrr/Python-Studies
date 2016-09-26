classspace = {}
parent_t = False

def create(n_class, parent):
    global classspace
    classspace.update({n_class: {'parent': parent}})
    return

def isParent(parent, n_class):
    if (classspace[n_class]['parent'] == None):
        # print("No")
        return
    elif (classspace[n_class]['parent'].count(parent) > 0):
        global parent_t
        parent_t = True
        return
    else:
        for i in range(len(classspace[n_class]['parent'])):
            isParent(parent, classspace[n_class]['parent'][i])


for _ in range(int(input())):
    strclass = input().split()
    if (len(strclass) == 1):
        create(strclass[0], None)
    else:
        create(strclass[0], strclass[2:])

for _ in range(int(input())):
    parent_t = False
    a = input().split()
    if (a[0] == a[1]):
        print("Yes")
    else:
        isParent(*a)
        if (parent_t):
            print("Yes")
        else:
            print("No")
