import sys
from tabulate import tabulate

def main():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    i = sys.argv[1]
    if i[-4:] != ".csv":
        print("Not a CSV file")
        sys.exit(1)
    csv = open_csv(i)
    print(tabulate(csv[0], csv[1], tablefmt="grid"))


def open_csv(file_path):
    lines = []
    table = []
    with open(file_path) as file:
        for _ in file:
            lines.append(_)
    header = lines[0].rstrip("\n").split(",")
    for _ in lines[1:]:
        table.append(_.rstrip("\n").split(","))
    return table, header
        

if __name__ == '__main__':
    main()