try:
 c='a'/0
except(ZeroDivisionError,TypeError):
 print("Divided by zero,type error")
else:
 print("No Error")
finally:
 print("Program executed")
