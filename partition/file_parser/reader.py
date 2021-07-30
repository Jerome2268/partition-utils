def read(path):
    file = open(path, mode="r")
    li = file.read(100000).strip().split("\n")
    return list(map(lambda s: s.strip(), li))


if __name__ == '__main__':

    for i in range(10200):
        print("木棉%s " % str(i))
