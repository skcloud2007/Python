## in this case finally block will not execute

import os
try:
  print("TRY")
  os._exit(0) ## PVM will shutdown
## 0 --> Normal Termination
except ValueError:
  print("Except")

finally:
  print("Finally")


## O/P --> TRY