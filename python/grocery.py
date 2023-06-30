list = []
sortlist = []
l = 1
c = 1

while True:
    try:
        while True:
            i = input()
            list.append(i)
    except(EOFError):
        print("\n")
        for _ in list[0:]:
            sortlist.append(str.upper(_))
        sortlist = sorted(sortlist)
        while True:
            try:
                for _ in sortlist[0:]:
                    if sortlist[l] == _:
                        f = sortlist[l]
                        sortlist.remove(f)
                        c = c + 1
                        continue
                    else:
                        l = l + 1
                        print(str(c) + " " + _)
                        c = 1
                        continue
            except(IndexError):
                print(str(c) + " " + _)
                break
    break