import random
def main():
    p = 0
    f = 0
    lvl = get_level()
    while True:
        try:
            for _ in range(0,10):
                x = generate_integer(lvl)
                y = generate_integer(lvl)
                #for __ in range(0,3):
                i = int(input(f"{x} + {y} = "))
                sol = x + y
                if i == int(sol):
                    p = p + 1
                else:
                    for __ in range(0,3):
                        print("EEE")
                        f = f + 1
                        #i = int(input(f"{x} + {y} = "))
                        if f == 3:
                            print(f"{x} + {y} = {sol}")
                            f = 0
                            break
                        else:
                            if i == int(sol):
                                break
                            else:
                                i = int(input(f"{x} + {y} = "))
            print(f"Score {p}")
            break
        except ValueError:
            pass

def get_level():
    while True:
        try:
            lvl = input("Level: ")
            lvl = int(lvl)

            if lvl < 1 or lvl > 3:
                pass
            else:
                return lvl
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        start = 0
    else:
        start = 10**(level - 1)
    end = (10**level) - 1
    integer = random.randint(start,end)
    return integer

if __name__ == '__main__':
    main()