# tipos variables 
#
# fuente https://learn.microsoft.com/es-es/training/modules/intro-to-python/ 
#
name = input('Enter your name:')
print(name)

print('What is your name?')
name = input()
print(name)

x = int(input('Enter a number: '))
print("x=",x)
print("el tipo de datos es ", type(x))

# Conversión de números en cadenas
x = 5.10
print('The number is ' + str(x))

first_number = int(input('Type the first number: ')) ;\
second_number = int(input('Type the second number: ')) ;\
print("The sum is: ", first_number + second_number)