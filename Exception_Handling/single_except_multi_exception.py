# Single except block will handle multiple exception 
try:
  x=int(input('Enter First Number:'))
  y=int(input('Enter Second Number:'))
  print('Result of: ', x/y)
except(ZeroDivisionError,ValueError) as msg: ## can define known exception in single except block
  print('Exception name: ', msg.__class__.__name__)
  print('Please provide valid input')