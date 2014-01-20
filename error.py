try:
 c=2/0
except(ZeroDivisionError):
 print("Divided by zero")
else:
 print("No Error")
finally:
 print("Program executed")
