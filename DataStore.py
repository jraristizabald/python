# Listas 
customerName = ['Marion Weaver', 'Alberto Mendoza', 'Katharine Tyler', 'Isaac Steele']
NombreCliente = ["Jorge R Aristizabal", "Maria P Merizalde", "Jorge A Aristizabl", "Catalina Aristizabal", "Santiago Aristizabl"]
# assign the value 'Marianne Weaver' to the first name in our list
# it is index 0, because indices start at 0 in python!
customerName[0] = 'Marianne Weaver'
print(customerName[0])
# print the last item
print(customerName[-1])

# access the second item to the 3rd
print(customerName[1:3])

# access all items from the beginning to the second
print(customerName[:2])
#los tres primeros elementos son números enteros, mientras que el último es un decimal
amountAccount = [10000, 150, 300, 1800.74]

strangeList = [4, 10.2, 'Marion Weaver', ['another list', 1]]
# print the 4th item of the list
print(strangeList[3])

# listas
list = [] # Crear lista vacia
list.append(7) # -> [7]
list.append(5) # -> [7, 5]
list.insert(1,12) # [7, 12, 5]
list[0] = 4 # -> [4, 12, 5]
list.remove(12) # [4, 5]
list.index(5) # prints 1
list.extend([1, 2, 3]) # [4, 5, 1, 2, 3]
del list[3] # [4, 5, 1, 3]
len(list) # will print 4

list1 = [1, 2, 3]
len(list1) # will print 3

colors = ['red', 'yellow', 'orange', 'green', 'blue']
colors[3] = 'emerald'
for color in colors :
    print(color)
# Diccionarios
# un diccionario es una lista de elementos organizados a través de un sistema de claves 
accounts = {'Marion Weaver': 10000, 'Alberto Mendoza': 150, 'Katharine Tyler': 300, 'Isaac Steele': 1800.74}
print(accounts['Alberto Mendoza']) # -> 150
print(accounts)
accounts['Marion Weaver'] -= 2000 # I subtract 2000 from David's account
accounts['Kristian Roach'] = 1000 # I add a new individual in my dictionary
print(accounts['Kristian Roach']) # I print the value of Kristian's account
print(accounts)
accounts.pop('Alberto Mendoza') # deletes Alberto Mendoza from our dictionary
print(accounts)
len(accounts) # -> 3

#  tuplas - son inmutables (no se pueden add o borrar elementos)
my_tuple = (1, 2, 3, 'a', 'b')
print(my_tuple[1]) # -> 2
print(my_tuple[4]) # -> 'b'

