i = input("Greeting: ")
i = i.lower().replace(" ","")

while True:
    if i.startswith("hello") is True:
        print("$0")
        break
    elif i.startswith("h") is True:
        print("$20")
        break
    else:
        print("$100")
        break