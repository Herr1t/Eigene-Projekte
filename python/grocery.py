list = []

while True:
    try:
        while True:
            i = input()
            list.append(i)
    except(EOFError):
        for i in list[0:]:
            
            print(str.upper(i))
        break