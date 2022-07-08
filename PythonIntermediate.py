# # Lists
# my_items = ['apple','banana','coconut']
# my_items_copied = my_items[:]
# my_items_copied.append('dragonfruit',)
# print(my_items)
# print(my_items_copied)

# # Tuples
# ''' What separates Tuples from Lists is () and []'''
# my_tuples = tuple(['Max',28, 'Boston'])

# print(my_tuples)

# Set
fruit = {'apple','banana','coconut'}
print(fruit)

for object in fruit:
    print(object)

fruit.add('cherry')
fruit.add('dragonfruit')

fruit2 = {'eggplant','fascell mango','grape'}
fruit.update(fruit2)
print(fruit)

fruit.remove('coconut')
print(fruit)