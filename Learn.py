# Time codes
from datetime import time
from time import strftime

print('Today\'s date is ' + str(strftime('%m/%d/%Y'))) 
print('and the time is ' + str(strftime('%H:%M:%S')))
print('and the timezone is GMT' + str(strftime('%z')))

# Global thing
name = 'Brad'

def Greetings():
    return 'Hello ' + name

def AlternativeName(new_name):
    global name
    name = new_name

AlternativeName('Bacon')
print(Greetings())

# Shape tings
import PythonShapeDrawing

print(PythonShapeDrawing.Rectangle(4,5))

# Easter Eggs
import this