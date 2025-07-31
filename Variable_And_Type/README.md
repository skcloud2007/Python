# Python Variable

Variables are essentially a name attached to a specific Python object that is stored in memory. Once the object has been assigned to the variable, the program can interact with the object through referencing the name. Unlike other programming languages, a variable in Python doesn’t need to be explicitly declared before using. For example, a variable called “x” can be created and assigned when needed.

```
Variable names must start with a letter or an underscore. Variables can not start with a number.
```

```
Variable names can be short, ie. “x”, or longer and more descriptive, ie. SalesTax.
```

```
Variable names are case sensitive. Ie. “x” and “X” would be considered two different variables.
```

```
Avoid using lowercase “l” and uppercase “I”, as well as uppercase “O”. These characters can cause confusion, because a lowercase “l” looks like an uppercase “I” and an uppercase “O” might look like an “0”.
```

## string Methods Reference
### str.capitalize()

Returns a copy of the string with its first character capitalized and the rest   lowercased.

```
Input: "python is awesome".capitalize()
Output: "Python is awesome"
```
### str.count(sub,[start],[end])
Returns the number of non-overlapping occurrences of substring
```
IN: "school".count("o")
OUT: 2
```
### str.find(sub,[start],[end])
Returns the lowest index in the string where substring "sub" is found within the string
```
IN: "school".find("o")
OUT: 3
```