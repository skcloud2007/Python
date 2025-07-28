try:
  x = int(input('Enter First Number:'))
  y = int(input('Enter Second Nuumber:'))
  print('The result:', x/y)
except BaseException as msg:
  print('The type of exception:', type(msg))
  print('The type of exception:', msg.__class__)
  print('The name of exception:', msg.__class__.__name__)
  print('The Description:', msg)