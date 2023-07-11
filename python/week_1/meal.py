def main():
    i = input("What time is it? ").replace(" ","")
    time = convert(i)
    if time <= 8.0 and time >= 7.0:
        print("breakfast time")
    elif time <= 13.0 and time >= 12.0:
        print("lunch time")
    elif time <= 19.0 and time >= 18.0:
        print("dinner time")
    else:
        pass


def convert(time):
    d = ""
    d = time[2:].replace(":","")
    d = int(d) / 60
    for _ in time:
        if _ == ":":
            time = time.replace(":","")
            if int(time) > 24:
                time = int(time[:-1])
            contime = int(time) + float(d)
            return float(contime)
        else:
            time = time[:-1]


if __name__ == "__main__":
    main()