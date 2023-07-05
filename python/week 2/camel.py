while True:
    try:
        i = input("camelCase: ").replace(" ","")
        print("snake_case: ", end="")
        for _ in i:
            if _ == _.upper():
                print(f"_{_.lower()}", end="")
            else:
                print(f"{_}", end="")
        print()
        break
    except IndexError:
        continue
