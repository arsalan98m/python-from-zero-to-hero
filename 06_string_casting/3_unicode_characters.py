"""
Unicode Characters

Python also supports Unicode escape sequence characters, which are used to 
represent Unicode characters. These characters are denoted by \u followed by a 
four-digit hexadecimal code.

For example, the Unicode character for the letter A is \u0041.

my_string = "Hello, \u0041!"
print(my_string)
"""
# -*- coding: utf-8 -*-
print(r"\u0041 =", "\u0041")  # Output: \u0041 = A
print(r"\u0042 =", "\u0042")  # Output: \u0042 = B
print(r"\u0043 =", "\u0043")  # Output: \u0043 = C
