# ********** string formatting **********


"""
string formatting:

Python provides several ways to format strings:

1. % Operator: my_string = 'Hello, %s!' % 'World'


- In Python, %s, %d, %c, %f are placeholders for values in a string. They are used with the % 
operator to insert values into a string.

- Note: The % operator is an older way of formatting strings in Python. The newer and more 
recommended way is to use the str.format() method or f-strings (introduced in Python 3.6). For 
example:

2. str.format(): my_string = 'Hello, {}!'.format('World')

3. f-Strings: my_string = f'Hello, {"World"}!'

Python String Formatting with % Placeholders:

| Placeholder | Meaning                            | Example                                     | Output            |
|-------------|-------------------------------------|---------------------------------------------|-------------------|
| %s          | String                             | "Hello, %s" % "Alice"                       | "Hello, Alice"    |
| %d          | Integer (Decimal)                  | "Age: %d" % 25                              | "Age: 25"         |
| %c          | Character                          | "Letter: %c" % 'A'                          | "Letter: A"       |
| %f          | Floating-point                     | "Pi: %f" % 3.14159                          | "Pi: 3.141590"    |
| %.nf        | Floating-point with n decimals     | "%.2f" % 3.14159                            | "3.14"            |

Note:
- `%s` can be used for any data type; Python will convert it to a string.
- `%f` by default prints 6 decimal places unless specified using `%.nf`.

"""
