def main():
    i = input("Input: ")
    ci = convert(i)
    print(f"{gauge(ci)}%")


def convert(fraction):
    a, b = fraction.split('/')
    a, b = int(a), int(b)
    if b == 0:
        raise(ZeroDivisionError)
    if a > b:
        raise(ValueError)
    rounded = int(round(float(a/b * 100)))
    return rounded


def gauge(percentage):
    output = ""

    if percentage >= 99:
        output += "F"
    elif percentage <= 1:
        output += "E"
    else:
        output += str(percentage + "%")
    return output


if __name__ == "__main__":
    main()