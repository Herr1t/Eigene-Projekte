names = []

def Input():
    while True:
        try:
            i = input("Name: ")
            names.append(i)
        except(EOFError):
            l = len(names)
            if l == 1:
                print(f"\nAdieu, adieu, to {names[0]}")
                break
            elif l == 2:
                print(f"\nAdieu, adieu, to {names[0]} and {names[1]}")
                break
            elif l > 2:
                print("\nAdieu, adieu, to ", end="")
                for _ in names[:-1]:
                    print(f"{_}, ", end="")
                print(f"and {names[-1]}")
                break
            else:
                break

if __name__ == '__main__':
    Input()