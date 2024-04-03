# tipos variables 
#
# fuente https://learn.microsoft.com/es-es/training/modules/intro-to-python/ 
#
x = 1         # assign variable x the value 1
y = x + 5     # assign variable y the value of x plus 5
z = y         # assign variable z the value of y
print("x=",x," Y=",y)
x = 1
print("x=",x)
print(type(x)) # outputs: <class 'int'>

x = 1.0
print("x=",x)
print(type(x)) # outputs: <class 'float'>

x = True
print("x=",x)
print(type(x)) # outputs: <class 'bool'>

x = 'This is a string'
print("x=",x) # outputs: This is a string
print(type(x)) # outputs: <class 'str'>
y = "This is also a string"
print("y=",y)
print("x+y",x+y)