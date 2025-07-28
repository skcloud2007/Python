## CASE 2 --> Exception raised and handled

try:
  print("Try")
  print(10/0)
except ZeroDivisionError:
  print("Except")

finally:
  print("finally")
## Here all been executed
