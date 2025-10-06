"""
Numeric Types in Python
------------------------

Python provides three primary numeric data types:

1️⃣ int (Integer)
-----------------
- Whole numbers (no decimal point)
- Can be positive, negative, or zero
- No size limit (Python handles large integers automatically)

Examples:
---------
x = 10
y = -5
z = 12345678901234567890

print(type(x))  # <class 'int'>
print(x + y)    # 5
print(z * 2)    # 24691357802469135780


2️⃣ float (Floating-Point)
---------------------------
- Numbers with decimal points
- Useful for scientific or precise calculations

Examples:
---------
a = 3.14
b = -0.75
c = 10.0

print(type(a))     # <class 'float'>
print(a + b)       # 2.39
print(c / 2)       # 5.0
print(round(a, 1)) # 3.1


3️⃣ complex (Complex Numbers)
------------------------------
- Numbers with a real and imaginary part: a + bj
- `j` represents the imaginary unit (like √-1)
- Mostly used in advanced math, physics, engineering

Examples:
---------
num1 = 2 + 3j
num2 = complex(5, -1)

print(type(num1))       # <class 'complex'>
print(num1 + num2)      # (7+2j)
print(num1.real)        # 2.0
print(num1.imag)        # 3.0


🔧 Useful Functions for Numeric Types:
-------------------------------------
abs(-7)          # 7 → Absolute value
int(5.9)         # 5 → Convert float to int (truncates)
float(3)         # 3.0 → Convert int to float
complex(1, 2)    # (1+2j) → Create a complex number
round(3.567, 2)  # 3.57 → Round to 2 decimal places
divmod(9, 4)     # (2, 1) → (quotient, remainder)

"""

# int (Integer)
x = 10
y = -5
z = 12345678901234567890

print("*" * 10 + "int example" + "*" * 10)
print(type(x))  # <class 'int'>
print(x + y)    # 5
print(z * 2)    # 24691357802469135780

# float (Floating-Point)
a = 3.14
b = -0.75
c = 10.0

print("*" * 10 + "float example" + "*" * 10)
print(type(a))     # <class 'float'>
print(a + b)       # 2.39
print(c / 2)       # 5.0
print(round(a, 1))  # 3.1

# complex (Complex Numbers)
num1 = 2 + 3j
num2 = complex(5, -1)

print("*" * 10 + "complex example" + "*" * 10)
print(type(num1))       # <class 'complex'>
print(num1 + num2)      # (7+2j)
print(num1.real)        # 2.0
print(num1.imag)        # 3.0

"""
what python does it allows us to separate numbers with underscores and this is for readability and it still being treated without the underscores just improves readability
"""
total_tea_leaves_harvested = 1_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")
