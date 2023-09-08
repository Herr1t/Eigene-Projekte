import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"^\<.+src=\"(https?://(?:www\.)?youtube\.com/embed/\w+)\".+\>$", s):
        output = re.sub(r"(https?://)?(www\.)?youtube.com/embed", "https://youtu.be", matches.group(1))
        return output
    return None


if __name__ == "__main__":
    main()