"""
Python Keywords
---------------

Keywords in Python are reserved words that have predefined meanings and roles in the language's syntax and structure.

These words:
- Cannot be used as variable, function, class, or identifier names.
- Control the flow, logic, and structure of Python programs.

Examples of Python keywords include:
-------------------------------------
False, True, None, and, or, not, if, else, elif, while, for, break, continue,
return, def, class, try, except, finally, raise, import, from, as, pass, global,
nonlocal, lambda, assert, yield, with, del, is, in, not, async, await, etc.

Example Usage:
---------------
def greet():         # 'def' is a keyword used to define a function
    return "Hello"   # 'return' is a keyword to return a value from a function

if True:             # 'if' and 'True' are keywords
    print("Yes")

Notes:
------
- Python is case-sensitive, so `True` is a keyword but `true` is not.
- To view all keywords in your current Python version, you can use:

    >>> import keyword
    >>> print(keyword.kwlist)
"""

import keyword

# Line continuation (`\`) allows printing a statement over multiple lines, improving code readability without breaking the string.
print("The list of \
keywords is : ")

# printing all keywords at once using "kwlist()"
print(keyword.kwlist)

# You cant use keywords / reserved words as variable name. Uncomment below line to see error
# and: bool = True
