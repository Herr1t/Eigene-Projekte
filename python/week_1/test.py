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

while True:
    i = input("File name: ")
    if "." not in i:
        print(other)
        break
    for _ in i:
        if _ == ".":
            if i in ending:
                print(ending[i])
                break
        i = i[1:]
    break