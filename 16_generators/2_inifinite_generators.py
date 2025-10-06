def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1


refill = infinite_chai()
user2 = infinite_chai()

print("refill")
for _ in range(5):
    print(next(refill))

print(next(refill))

print("user2")
for _ in range(6):
    print(next(user2))
