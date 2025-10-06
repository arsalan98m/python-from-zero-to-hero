
# Dynamically Created Strings: Strings created at runtime (e.g., concatenation) are not interned or pooled.

a = "hello"
b = "world"
c = a + b  # dynamically created string
d = "helloworld"
print("c is d = ", c is d)  # False (not interned or pooled)
print(c, " - id(c)", id(c))
print(d, " - id(d)", id(d))

c1 = a + b
print("c is c1 = ",  c is c1)  # False (not interned or pooled)

print(c1, " - id(c1)", id(c1))
print(c,  " - id(c) ", id(c))

print("is content same = ", c == c1)
