##Every exception is a class 
# ZeroDivisionError -->> PVM take cares
print("Hello")
try:
  print(10/0)
except ZeroDivisionError:
  print('Hi') ## can not execute because of ZeroExceptionError