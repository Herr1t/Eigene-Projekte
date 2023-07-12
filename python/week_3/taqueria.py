import sys
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
t = 0
while True:
    try:
        i = input("Item: ")
        item = i.title()
        if item in menu:
            #print(menu[i])
            t = t + menu[item]
            print("Total: ${0:0.2f}".format(t))
            continue
    #except(ValueError):
        #continue
    except(EOFError):
        sys.exit()