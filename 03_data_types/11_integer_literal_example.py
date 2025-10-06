shark1_age = 300
shark2_age = 300

print("Value of shark1_age = " + str(shark1_age) +
      ", and id(shark1_age) = " + str(id(shark1_age)))
print("Value of shark2_age = " + str(shark2_age) +
      ", and id(shark2_age) = " + str(id(shark2_age)))

if (shark1_age == shark2_age):  # comparison by value True
    print("shark1_age & shark2_age have same age")
else:
    print("shark1_age & shark2_age have different age")

print(" ===================== ")

if (id(shark1_age) == id(shark2_age)):  # comparison by id() False
    print("shark1_age & shark2_age have same id")
else:
    print("shark1_age & shark2_age have different id")
