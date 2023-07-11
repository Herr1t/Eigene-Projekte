import sys
from random import choice
from pyfiglet import FigletFont
from pyfiglet import Figlet
from pyfiglet import FontNotFound

def Processing():
    g = FigletFont.getFonts()
    while True:
        try:
            if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                f = Figlet(font=sys.argv[2])
                i = input("Input: ")
                print(f.renderText(i))
                sys.exit()
            else:
                sys.exit("Invalid Usage")
        except(FontNotFound):
            sys.exit("Invalid Usage")
        except(IndexError):
            f = Figlet(font=choice(g))
            i = input("Input: ")
            print(f.renderText(i))
            sys.exit()

if __name__ == '__main__':
    Processing()