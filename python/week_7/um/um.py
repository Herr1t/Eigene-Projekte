import re


def main():
    print(count(input("Text: ")))


def count(s):
    if um := re.findall(r"(Um| um)[,.?!]", s):
        return len(um)
    if s == "um":
        return "1"


if __name__ == "__main__":
    main()