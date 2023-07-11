def main():
    i = input("Input: ")
    #omitted = shorten(i)
    print(f"Output: {shorten(i)}")


def shorten(word):
    vowels_upper = ["A", "E", "I", "O", "U"]
    vowels_lower = ["a", "e", "i", "o", "u"]
    oword = ""

    for _ in word:
        if _ in vowels_lower:
            #word.replace(_,"")
            continue
        if _ in vowels_upper:
            #word.replace(_,"")
            continue
        else:
            oword += _
    return oword


if __name__ == "__main__":
    main()