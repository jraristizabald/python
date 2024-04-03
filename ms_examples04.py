# tipos variables 
#
# fuente https://learn.microsoft.com/es-es/training/modules/python-create-run-program
# https://www.w3schools.com/python/python_datetime.asp

from datetime import date
print(date.today())
print("Today's date is: " + str(date.today()))
x = date.today()

print("hoy =", x.today())
print("Año =", x.year)
print("Dia =",x.strftime("%A"))
print("mes =",x.strftime("%B"))

