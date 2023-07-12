import random
import matplotlib.pyplot as plt

class Object:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def check_overlap(obj1, obj2):
    if obj1.x < obj2.x + obj2.width and obj1.x + obj1.width > obj2.x and \
       obj1.y < obj2.y + obj2.height and obj1.y + obj1.height > obj2.y:
        return True
    return False

def generate_objects(num_objects):
    objects = []
    while len(objects) < num_objects:
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        width = random.randint(1, 10)
        height = random.randint(1, 10)
        new_object = Object(x, y, width, height)
        if x + width <= 100 and y + height <= 100:
            overlap = False
            for obj in objects:
                if check_overlap(new_object, obj):
                    overlap = True
                    break
            if not overlap:
                objects.append(new_object)
    return objects

def calculate_area(objects):
    area = 0
    for obj in objects:
        area += obj.width * obj.height
    return area

def plot_objects(objects):
    plt.figure(figsize=(6, 6))
    ax = plt.gca()
    ax.set_xlim([0, 100])
    ax.set_ylim([0, 100])
    for obj in objects:
        rect = plt.Rectangle((obj.x, obj.y), obj.width, obj.height, facecolor='blue', alpha=0.5)
        ax.add_patch(rect)
    plt.show()

def main():
    objects = []
    max_objects = 64
    max_area = 10000  # 100 * 100
    while len(objects) < max_objects and calculate_area(objects) < 0.8 * max_area:
        new_objects = generate_objects(max_objects - len(objects))
        objects.extend(new_objects)
    print("Total number of objects:", len(objects))
    print("Total area occupied:", calculate_area(objects))
    plot_objects(objects)

if __name__ == '__main__':
    main()