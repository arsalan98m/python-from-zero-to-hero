

# Process = Interning
# Memory Space = Pool of String Literals

# When Are Strings Not Interned or Pooled?


import sys

# Long Strings: Strings longer than 20 characters are usually not interned automatically.
# (make sure to run this this code in google colab for better results)


a = "this is a very long string"
b = "this is a very long string"
print(a is b)  # False (not interned)
print("id(a)", id(a))  # 138806975824480
print("id(b)", id(b))  # 138806975870848


a = sys.intern("this is a very long string")
b = sys.intern("this is a very long string")
print(a is b)  # True (interned)
print("id(a)", id(a))  # 138806975824480
print("id(b)", id(b))  # 138806975824480
