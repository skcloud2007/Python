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
### str.isalpha()
Return true if all characters in the string are alphabet and there is atleast one character.
```
IN: "Python".isalpha()
OUT: True
IN: "Python3".isalpha()
OUT: False
```
### str.isdigit()
Returns   true if all characters in the string are digits and there is at least one   character.
```
IN: "123".isdigit()
OUT: True
IN: "123a".isdigit()
OUT: False
```
### str.upper()

Returns a copy of the   string with all the cased characters converted to uppercase.

```
IN: “python”.upper()
OUT: “PYTHON”
```


### str.lower()
Returns a copy of the string with all the cased characters converted to lowercase.

```
IN: “PYTHON”.lower()
OUT: “python”
```
### str.split([sep],[maxsplit])

Returns a list of the   words in the string, using sep as the delimiter string.

IN:          “String,Methods”.split(“,”)

OUT:      [“String”, “Methods”]



str.strip([chars])

Returns   a copy of the string with the leading and trailing characters removed.

IN:          “     python   “.strip()

OUT:      “python”



Str.title()

Return a titlecased   version of the string where words start with an uppercase character and the   remaining characters are lowercase.

IN:          “python is awesome”.title()

OUT:      “Python Is Awesome”



For a complete list of String   Methods, visit: https://docs.python.org/release/2.5.2/lib/string-methods.html   

Resources for this lecture