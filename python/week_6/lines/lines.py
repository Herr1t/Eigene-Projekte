import sys

def main():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    i = sys.argv[1]
    if i[-3:] != ".py":
        print("Not a Python file")
        sys.exit(1)
    file = file_open(i)
    print(line_counting(file))
            


def file_open(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content


def line_counting(content):
    lines = []
    for _ in content:
        _ = _.replace(" ","")
        if _ == "\n":
            continue
        elif _[0] == "#":
            continue
        lines.append(_)
    return len(lines)


if __name__ == '__main__':
    main()