def main():
    plate = str(input("Plate: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l = len(s)
    c = 0
    if l < 2 or l > 6:
        return False
    begin = str(s[:2])
    #end = str(s[-1:])
    number = ""
    for _ in s:
        if _.isdigit() is True:
            number += _
            check = s[c:]
            break
        elif _.isalpha() is False and _.isdigit() is False:
            return False
        c = c + 1
    if begin.isalpha() is False:
        return False
    if bool(number) is True:
        if check.isdigit() is False:
            return False
        if int(number[:1]) == 0:
            return False
        return True
    return True


main()