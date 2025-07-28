# Valid Syntax for Defining `except` Block in Python

This document outlines various valid syntax options for handling exceptions in Python using the `except` block. Below are the different ways you can catch specific, multiple, or all exceptions, and how to properly use them in your code.

## 1. **Handling a Specific Exception**
To catch a specific exception, such as `ZeroDivisionError`, you can use the following syntax:

```python
except ZeroDivisionError:

except ZeroDivisionError:

except (ZeroDivisionError):

except ZeroDivisionError as msg:

except (ZeroDivisionError) as msg:

except (ZeroDivisionError, ValueError):

except(ZeroDivisionError, ValueError) as e:

except:
```

# 2. **Finally block vs Destructor**
Finally block meant for maintaining cleanup code Also Desctructor meant for maintaining cleanup code. Seems both are same Then Where is the difference:
``` finally always relates with try block while for destructor always used to do cleanup for object related, whatever resource allocated inside destructor, whill be executed before destroying Object.
