
"""
Strings in Python

In Python, a string is a sequence of characters enclosed in quotes (either single, double, or triple quotes).
Strings are immutable, meaning they cannot be changed after they are created.

Creating Strings
- Single quotes: 'Hello, World!'
- Double quotes: "Hello, World!"
- Triple quotes: '''Hello, World!''' (can span multiple lines)
- Raw strings: r"Hello, World!"  (treats backslashes as literal characters)
"""

# For multi-line strings, use triple quotes ''' or """
my_multiline_string = '''Hello,
                    \t\n\n\nWorld!
'''
print(my_multiline_string)


my_string: str = r"Hello\t,\nWorld\d"
print(my_string)

my_string2: str = "Hello,\n World!"
print(my_string2)
