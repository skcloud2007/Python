## PVM will check in defined order from top to bottom
try:
  x=int(input('Enter First Number:'))
  y=int(input('Enter Second Number:'))
  print('Result of: ', x/y)
except ZeroDivisionError:
  print('Cant divide with zero')
except ValueError:
  print('Please provide init value')

