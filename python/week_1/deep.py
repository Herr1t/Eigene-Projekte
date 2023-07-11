i = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
i = i.lower()

if "42" in i or "forty-two" in i or "forty two" in i:
    print("Yes")
else:
    print("No")