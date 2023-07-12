import sys
import csv

students = []

def main():
    while True:
        try:
            if len(sys.argv) > 3:
                print("Too many command-line arguments")
                sys.exit(1)
            if len(sys.argv) < 3:
                print("Too few command-lines arguments")
                sys.exit(1)
            before = sys.argv[1]
            after = sys.argv[2]
            open(before)
            scourgify(before, after)
            sys.exit(0)
        except FileNotFoundError:
            print(f"Could not read {before}")
            sys.exit(1)


def scourgify(before, after):
    names = []
    houses = []
    with open(before) as bfile:
        reader = csv.DictReader(bfile)
        for row in reader:
            names.append(row['name'].split(","))
            houses.append(row['house'])
    while True:
        c = 0
        for _ in names:
            names[c].append(houses[c])
            c = c +1
        break
    with open(after, "w") as afile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(afile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in names:
            writer.writerow({'first': _[1].replace(" ",""), 'last': _[0], 'house': _[2]})
    return 0


if __name__ == '__main__':
    main()