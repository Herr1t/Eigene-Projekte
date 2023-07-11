month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
y = 0
x = 1
while True:
    i = input("Date: ")
    si = i
    while True:
        for _ in si[0:]:
            if _ == ",":
                si = i.split()
                si =([z.strip(' ') for z in si])
                if (any(c == si[0] for c in month[0:])) is False:
                    si[1] = 32
                else:
                    si = ([s.strip(',') for s in si])
                break
            elif _ == "/":
                si = i.split('/')
                si = ([z.strip(' ') for z in si])
                if (any(c == si[0] for c in month[0:])) is True:
                    si[1] = 32
                elif int(si[0]) < 1 or int(si[0]) > 12:
                    si[1] = 32
                break
            else:
                continue
        break
    if si == i:
        si = i.split()
        si[1] = 32
    if int(si[1]) < 1 or int(si[1]) > 31:
        continue
    elif len(si) == 3:
        while True:
            try:
                for f in si[y:]:
                    if int(f) < 10:
                        si[y] = ('0'+ f)
                        y =+ 1  
                        continue
                    elif (any(f == si[y] for f in month[0:])) is True:
                        y =+ 1
                        continue
                    elif y == 2:
                        break
                    else:
                        y =+ 1
                        continue
                break
            except(ValueError):
                y =+ 1
                continue
        break
    else:
        continue

for _ in month[0:]:
    if _ == si[0]:
        if x < 10:
            print(si[2],'0' + str(x),si[1], sep="-")
        else:
            print(si[2],str(x),si[1], sep="-")
        break
    elif si[0] == '0' + str(x):
        print(si[2],si[0],si[1], sep="-")
        break
    elif si[0] == str(x):
        print(si[2],si[0],si[1], sep="-")
        break
    else:
        x = x + 1
        continue