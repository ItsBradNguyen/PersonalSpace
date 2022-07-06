print('Hello User! My name is PythonCalculator.')
print('With me, you can calculate Basic arithmetics,') 
print('find Circumference and Area of certained geometric shapes.')
function = input('What would you like to me to do or find? ')

# Basic Arithmetic Function
if function == 'Basic':
    num1 = int(input('Enter a number: '))
    op = input('Enter an operator: ')
    num2 = int(input('Enter a second number: '))

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    else:
        print('Invalid Operator!')

# Circumference Finder
elif function == 'Circumference':
    shape = input('What is the geometric shape of the object? ')
    from math import pi

    if shape == 'Triangle':
        side1 = int(input('What is the measurement of the first side? '))
        side2 = int(input('What is the measurement of the second side? '))
        side3 = int(input('What is the measurement of the third side? '))
        print('The circumference of the triangle is ' + str(side1 + side2 + side3))
    elif shape == 'Rectangle':
        side1 = int(input('What is the measurement of the first side? '))
        side2 = int(input('What is the measurement of the second side? '))
        print('The circumference of the rectangle is ' + str(2 * (side1 + side2)))
    elif shape == 'Square':
        side = int(input('What is the measurement of one side? '))
        print('The circumference of the square is ' + str(4 * side))
    elif shape == 'Circle':
        radius = int(input('What is the measurement of the radius? '))
        print('The circumference of the circle is ' + str(2 * pi * radius))
    else:
        print('Invalid Shape!')

# Area Finder
elif function == 'Area':
    shape = input('What is the geometric shape of the object? ')
    from math import pi

    if shape == 'Triangle':
        base = int(input('What is the measurement of the base? '))
        height = int(input('What is the measurement of the height? '))
        print('The area of the triangle is ' + str(0.5 * base * height))
    elif shape == 'Rectangle':
        side1 = int(input('What is the measurement of the first side? '))
        side2 = int(input('What is the measurement of the second side? '))
        print('The area of the rectangle is ' + str(side1 * side2))
    elif shape == 'Square':
        side = int(input('What is the measurement of one side? '))
        print('The area of the square is ' + str(pow(side,2)))
    elif shape == 'Circle':
        radius = int(input('What is the measurement of the radius? '))
        print('The area of the circle is ' + str(pi * pow(radius,2)))
    else:
        print('Invalid Shape!')

#Other
else:
    print('Invalid function!')