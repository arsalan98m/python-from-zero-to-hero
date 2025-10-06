"""
Commonly Used String Methods in Python:

1. split(delimiter):
   Splits a string into a list of substrings based on the specified delimiter.
   Example:
       text = "apple,banana,cherry"
       result = text.split(",")
       # Output: ['apple', 'banana', 'cherry']

2. join(iterable):
   Joins elements of a list (or any iterable) into a single string, using the string as a separator.
   Example:
       words = ['Hello', 'World']
       result = " ".join(words)
       # Output: 'Hello World'

3. replace(old, new):
   Replaces all occurrences of a substring with another substring.
   Example:
       text = "I love apples"
       result = text.replace("apples", "oranges")
       # Output: 'I love oranges'

4. find(substring):
   Returns the index of the first occurrence of the specified substring.
   Returns -1 if the substring is not found.
   Example:
       text = "Hello World"
       index = text.find("World")
       # Output: 6

5. index(substring):
   Returns the index of the first occurrence of the specified substring.
   Raises ValueError if the substring is not found.
   Example:
       text = "Hello World"
       index = text.index("World")
       # Output: 6

6. count(substring):
   Returns the number of times a substring appears in the string.
   Returns 0 if the substring is not found.
   Example:
       text = "banana"
       occurrences = text.count("a")
       # Output: 3

       missing = text.count("z")
       # Output: 0
"""
