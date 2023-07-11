while True:
    try:
        m = int(input("m: "))
        e = m * (300000000**2)
        print(f"e: {e}")
        break
    except ValueError:
        continue