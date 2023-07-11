due = 50
owed = 0
print(f"Amount Due: {due}")
while True:
    try:
        i = int(input("Insert Coin: "))
        if i == 25 or i == 10 or i == 5:
            owed = int(due) - i
            due = owed
        else:
            print(f"Amount Due: {due}")
            continue

        if owed == 0:
            print("Change Owed: 0")
            break
        if owed < 0:
            print(f"Change Owed: {owed * -1}")
            break
        print(f"Amount Due: {owed}")
        continue
    except ValueError:
        continue