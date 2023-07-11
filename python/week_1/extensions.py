from sys import exit
ending = {
".gif": "image/gif",
".jpg": "image/jpeg",
".jpeg": "image/jpeg",
".png": "image/png",
".pdf": "application/pdf",
".txt": "text/plain",
".zip": "application/zip" }
other = "application/octet-stream"

i = input("File name: ")
i = i.lower().replace(" ","")

while True:
    if not "." in i:
        print(other)
        break
    for _ in i:
        if _ == ".":
            if i in ending:
                print(ending[i])
                break
            else:
                i = i[1:]
                for __ in i:
                    if __ == ".":
                        if i in ending:
                            print(ending[i])
                            exit(1)
                    else:
                        i = i[1:]
                print(other)
                break
        else:
            i = i[1:]
    break