#try:
#    statement-1
#    statement-2
#    ststement-3
#except xxx:
#    statement-4
#statment-5

###########
# if no exception all statement will be executed
# if one exception raised at statement-2 and corresponding except block match then 1,4,5 has normal termination
# if an exception raised at statement-2, but corresponding except block not matched --> 1, Abnormal exception

try:
  print(10/0)
except ZeroDivisionError as msg:  ## msg created as Object
  print('The type of exception:', type(msg)) ## O/P --> The type of exception: <class 'ZeroDivisionError'>
  print('The type of exception:', msg.__class__)  ## O/P --> The type of exception: <class 'ZeroDivisionError'>
  print('The exception class name:', msg.__class__.__name__) ## O/P --> The exception colass name: ZeroDivisionError
  print('The description of exception:', msg) ## The description of exception: division by zero