import glob
import os
import re

subs = {}
dels = {"się", "i", "oraz", "nigdy", "dlaczego"}

def repl(m):
    word = m.group(1)
    if word in dels:
        return ""
    if word in subs:
        return subs[word] + m.group(2)
    return word + m.group(2)

for fpath in glob.iglob("textfiles_pl/*orgi.txt"):
    if not os.path.isfile(fpath):
        print("skipping", fpath)
        continue

    with open(fpath, "r") as f:
        inData = f.read()

    outData = re.sub(r"(\w+)(\W|$)", repl, inData)
    newFpath = fpath.replace(".orgi.txt", ".del.txt")
    with open(newFpath, "w") as f:
        f.write(outData)
