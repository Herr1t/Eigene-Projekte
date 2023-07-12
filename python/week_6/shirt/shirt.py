import sys
from PIL import Image

images = []

def main():
    while True:
        try:
            if len(sys.argv) > 3:
                print("Too many command-line arguments")
                sys.exit(1)
            if len(sys.argv) < 3:
                print("Too few command-lines arguments")
                sys.exit(1)
            input = sys.argv[1]
            output = sys.argv[2]
            if input[-4:] != ".jpg" and input[-4:] != ".png" and input[-5:] != ".jpeg":
                raise FileNotFoundError
            if output[-4:] != ".jpg" and output[-4:] != ".png" and output[-5:] != ".jpeg":
                raise FileNotFoundError
            if input[-4:] != output[-4:] and input[-5:] != output[-5:]:
                print("Input and output have different extensions")
                sys.exit(1)
            open(input)
            overlap(input, output)
            sys.exit(0)
        except FileNotFoundError:
            print("Invalid input")
            sys.exit(1)


def overlap(input, output):
    for arg in sys.argv[1:]:
        image = Image.open(arg)
        images.append(image)

    images[0].save(
        "output.png", save_all=True, append_images=[images[1]]
    )


if __name__ == '__main__':
    main()