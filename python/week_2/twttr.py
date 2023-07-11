vowels_upper = ["A", "E", "I", "O", "U"]
vowels_lower = ["a", "e", "i", "o", "u"]

i = input("Input: ")
print("Output: ", end="")
for _ in i:
    if _ in vowels_lower:
        i.replace(_,"")
    elif _ in vowels_upper:
        i.replace(_,"")
    else:
        print(_, end="")
print()
