import os

wpath = "/home/kubuxu/.config"

def walk(path):
    print(path + "/")
    files = os.listdir(path)
    for f in files:
        p = os.path.join(path, f)
        if os.path.isdir(p):
            walk(p)
        else:
            print(p)


walk(wpath)

