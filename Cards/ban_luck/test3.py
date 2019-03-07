

d = {1:'a', 2:'b', 3:'c'}

with open("tst.txt") as f:
    for line in f:
       (key, val) = line.split()
       d[int(key)] = val
