# # Exponential Function
# def expfunc(base_num, pow_num):
#     result = 1
#     for i in range(0, pow_num):
#         result = result * base_num
#     return result    
    
# # 2D Grid & Nested Loops
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]

# for row in number_grid:
#     for col in row:
#         print(col)

# # Basic Translator
# def translate(phrase):
#     translation = ''
#     for letter in phrase:
#         if letter in 'AEIOUaeiou':
#             translation = translation + 'g'
#         else:
#             translation = translation + letter
#     return translation

# print(translate('flabbergaste'))

# # Try / Except
# try:
#     number = int(input('Enter a number: '))
#     print(number)
# except ValueError as error:
#     print(error)

# # Read Files
# ''' Can change 'r' into 'w' for write or 'r+' for read and write'''
# employee_file = open('Employees.txt', 'r')
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()

# # Writing To Files
# ''''a' stands for append'''
# employee_file = open('Employees.txt', 'w')
# employee_file.write('Jim - Salesman\nDwight - Salesman\nPam - Receptionist\nMichael - Manager\nOscar - Accountant\nTobey - Human Resources\nKelley - Customer Service')
# employee_file.close()

# #Classes & Objects
# from PythonClass import Student
# student1 = Student('Brad','Information System', 3.974, False)
# print(student1.is_on_probation)

# # Object Functions
# class Student:
#     def __init__(self, name, major, gpa):
#         self.name = name
#         self.major = major
#         self.gpa = gpa
#     def on_honor_roll(self):
#         if self.gpa >= 3.5:
#             return True
#         else:
#             return False

    
# Student1 = Student('Oscar', 'Accounting', 3.1)
# Student2 = Student('Mya', 'Business', 4)

# print(Student2.on_honor_roll())

# # Inheritance
# from argparse import _MutuallyExclusiveGroup


# class Chef:
#     def make_chicken(self):
#         print('The chef makes a chicken.')
#     def make_salad(self):
#         print('The chef makes a salad.')
#     def make_special_dish(self):
#         print('The chef makes bbq ribeyes.')

# class ChineseChef(Chef):
#     def make_special_dish(self):
#         print('The chef makes orange chicken.')
#     def make_fried_rice(self):
#         print('The chef makes fried rice.')

# myChef = Chef()
# myChef.make_special_dish()

# myChineseChef = ChineseChef()
# myChineseChef.make_chicken()

# Python Interpreter
