def main():
    i = input("Greeting: ")
    print(f"${value(i)}")


def value(greeting):
    greeting = greeting.lower().replace(" ","")
    money = 0
    if greeting.startswith("hello") is True:
        money =+ 0
    elif greeting.startswith("h") is True:
        money =+ 20
    else:
        money =+ 100
    return money


if __name__ == "__main__":
    main()