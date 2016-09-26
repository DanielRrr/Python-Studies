d = {"global": {"parent": None, "vars": []},}

def create_name_sp(ns, p):
    global d
    d.update({ns : {"parent": p, "vars": []}})

def add_var(ns, var):
    global d
    d[ns]["vars"].append(var)

def get_var(ns, var):
    global d
    if var in d[ns]["vars"]:
        return ns
    elif ns == "global" and var not in d["global"]["vars"]:
        return None
    else:
        return get_var(d[ns]["parent"], var)

for _ in range(int(input())):
    a = input().split()
    if a[0] == "create":
        create_name_sp(a[1], a[2])
    elif a[0] == "add":
        add_var(a[1], a[2])
    elif a[0] == "get":
        print(get_var(a[1], a[2]))
