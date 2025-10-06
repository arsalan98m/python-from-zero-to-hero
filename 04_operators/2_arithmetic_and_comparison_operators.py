# 2. Binary Operators
# Binary operators work with two operands (values or variables). They perform operations between two things.

# 2.1. Arithmetic Operators
# Arithmetic operators are used to perform mathematical operations on numbers.

a: int = 10
b: int = 3
print("a + b  = ", a + b)   # 13 Addition
print("a - b  = ", a - b)   # 7 Subtraction
print("a * b  = ", a * b)   # 30 Multiplication
print("a / b  = ", a / b)   # 3.3333333333333335
print("a // b = ", a // b)  # 3 Floor Division
# 1 Modulus (remainder) => // preserves float type when any operand is a float. agar koi bhi ek operand float h toh float return karega.
print("a % b  = ", a % b)
print("a % b  = ", a ** b)  # 1000 Exponentiation (10 * 10 * 10)

# 2.2. Comparison Operators
# Comparison operators are used to compare two values.

a: int = 10
b: int = 3
print("a == b = ", a == b)  # False Equal to
print("a != b = ", a != b)  # True Not Equal to
print("a > b  = ", a > b)   # True Greater than
print("a < b  = ", a < b)   # False Less than
print("a >= b = ", a >= b)  # True Greater than or Equal to
