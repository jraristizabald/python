#
name = input( 'What is your name, dear stranger?')

if len(name) > 0:
    print("Hello", name, "!")
else:
    print("Hello, world!")
    
thisCourseIsGreat = True
itsAuthorIsVeryHumble = False
weather = "The weather is great!"
weather.startswith("The weather") # -> True

myList = [4, 2, 3, 2, 10]
myStringList = ["a", "b", "c", "d"]
myString = "The weather is really good today!"

4 in myList # True
0 in myList # False
0 in myStringList # False
"c" in myStringList # True
"e" in myStringList # False
"weather" in myString # True
"really" in myString # True
"rain?" in myString # False

account = input("What is your account balance?")
account = int(account) # transform the answer into an integer

if account >= 10000:
    print("Loan granted!")
elif account >= 100 and account < 10000:
    print("Loan in process of validation: under study")
else:
    print("Loan refused")
