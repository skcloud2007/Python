# if no other blcok matched then default except block will be executed
# -->>>> except: <<<-----
try:
  x = int(input('Enter first number:..'))
  y = int(input('Enter Second number:..'))
  print('The result is..', x/y)

except ZeroDivisionError: ## Only handle "ZeroDivisionError"
  print('ZeroDivisonError:: divide by zero')

except: ## It handles all exception except "ZeroDivisionError"
  print('Default Except block: Provide int value')

