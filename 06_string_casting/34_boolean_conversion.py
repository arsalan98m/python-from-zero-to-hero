# ********** Boolean Conversion **********

# Converts other data types to boolean (True or False).


print("bool(1)       = ", bool(1))       # True
print("bool(0)       = ", bool(0))       # False
print("bool(-0)     = ", bool(-0))     # False
print("bool(+0)     = ", bool(+0))     # False
print("bool(0.0)     = ", bool(0.0))     # False
print("bool(-10)     = ", bool(-10))     # True (Non-zero numbers are True)
print('bool("")      = ', bool(""))      # False (Empty string)
print('bool("Hello") = ', bool("Hello"))  # True (Non-empty string)
print("bool([])      = ", bool([]))      # False (Empty list)
print("bool([1, 2])  = ", bool([1, 2]))  # True (Non-empty list)
