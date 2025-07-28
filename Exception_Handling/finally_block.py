## It will executed always irrespective of whether exception raised or not raised and whether exception handled or not handled.
## CASE: 1

try:
  print("try") ## will execute
except:
  print("Except") ## Ignored because of no exception

finally:
  print("Finally") ## Always exceute

## CASE:2
