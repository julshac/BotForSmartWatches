def tickets():
    t = {}
    for i in range(11):
        f = open("data/{}.txt".format(i), "r")
        t.update({f.readline()[:-1]: f.readline()})
    return t


ticket = tickets()
