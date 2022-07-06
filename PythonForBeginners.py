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

# Writing To Files
''''a' stands for append'''
employee_file = open('Employees.txt', 'w')
employee_file.write('Jim - Salesman\nDwight - Salesman\nPam - Receptionist\nMichael - Manager\nOscar - Accountant\nTobey - Human Resources\nKelley - Customer Service')
employee_file.close()


