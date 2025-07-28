## Exception raised but not handled

try:
  print("try")
  print(10/0)
except ValueError:
  print("Except")

finally:
  print("finally")

### print of try will execute then finally will execute then execption error will come