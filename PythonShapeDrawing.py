Char = '.'
# Rectangle
def Rectangle(height, width):
    for row in range(height):
        for col in range(width):
            print(Char, end = '')
        print()

# Square
def Square(side):
    return Rectangle(side,side)

# Triangle
def Triangle(height, width):
    for row in range(height):
        for col in range(1, row + 2):
            print(Char, end = '')
        print()


