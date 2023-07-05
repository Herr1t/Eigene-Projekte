def convert(i):
    if ":)" in i:
        i = i.replace(":)","🙂")
    if ":(" in i:
        i = i.replace(":(","🙁")
    print(i)

if __name__ == '__main__':
    i = input()
    convert(i)