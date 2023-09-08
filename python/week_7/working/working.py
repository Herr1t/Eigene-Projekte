import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    count = 1
    x = 0
    time = []
    if matches := re.search(r"^((\d{1,2})(?::\d{2})?) (AM|PM) to ((\d{1,2})(?::\d{2})?) (AM|PM)$", s):
        if int(matches.group(2)) > 12 or int(matches.group(5)) > 12 or int(matches.group(2)) == 0 or int(matches.group(5)) == 0:
            raise ValueError
        while count < 5:
            if ":" in matches.group(count):
                _ = matches.group(count).split(":")
                if int(_[1]) > 59:
                    raise ValueError
            if matches.group(count+2) == "AM" and re.search(r"^12(:\d{2})?$", matches.group(count)):
                time.insert(
                    x, re.sub(r"12", "00", matches.group(count)))
            elif matches.group(count+2) == "AM" and matches.group(count+1) != "12":
                time.insert(x, "0" + matches.group(count))
            elif matches.group(count+2) == "PM" and matches.group(count+1) != "12":
                time.insert(x, re.sub(matches.group(
                    count+1), str(int(matches.group(count+1))+12), matches.group(count)))
            else:
                time.insert(x, matches.group(count))
            if ":" not in time[x]:
                time[x] = re.sub(time[x], time[x] + ":00", time[x])
            count = count + 3
            x = x + 1
        return (f"{time[0]} to {time[1]}")
    raise ValueError


if __name__ == "__main__":
    main()