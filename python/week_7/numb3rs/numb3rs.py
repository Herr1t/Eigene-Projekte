import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    count = 1
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        while count < 5:
            part = int(matches.group(count))
            if part > 255 or part < 0:
                return False
            count += 1
    else:
        return False
    return True


if __name__ == "__main__":
    main()