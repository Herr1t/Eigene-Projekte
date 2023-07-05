import random
def main():
    while True:
        try:
            lvl = input("Level: ")
            lvl = int(lvl)
            if lvl <= 0:
                pass
            else:
                break
        except ValueError:
            pass

    goal = random.randint(1,lvl)
    goal = int(goal)

    while True:
        try:
            guess = input("Guess: ")
            guess = int(guess)

            if  guess > 0:
                if guess > goal:
                    print("Too large!")
                elif guess < goal:
                    print("Too small!")
                else:
                    print("Just right!")
                    break
        except ValueError:
            pass

if __name__ == '__main__':
    main()