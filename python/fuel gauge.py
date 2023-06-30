while True:
    try:
        a, b = input("Input: ").split('/')
        a, b = int(a), int(b)
    except(ValueError):
        continue
    try:
        fuel = int(a/b * 100)
    except(ZeroDivisionError):
        continue
    if fuel > 100:
        continue
    elif fuel >= 99:
        print("F")
        break
    elif fuel <= 1:
        print("E")
        break
    else:
        print(str(fuel) + '%')
        break