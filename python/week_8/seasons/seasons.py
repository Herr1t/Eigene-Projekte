from datetime import date
import re
import sys
import inflect

def main():
    p = inflect.engine()
    print((p.number_to_words(inputd(input("Date of Birth: ")), andword="")).capitalize() + " minutes")


def inputd(birth_date):
    try:
        _ = date.fromisoformat(birth_date)
        return output(birth_date)
    except ValueError:
        sys.exit("Inavild date")


def output(birth_date):
    birth = date.fromisoformat(birth_date)
    today = date.today()
    time = re.findall(r'\b\d+', str(date.__sub__(today, birth)))[0]
    return (int(time) * 24 * 60)


if __name__ == "__main__":
    main()