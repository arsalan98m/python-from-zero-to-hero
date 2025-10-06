is_boiling = True
str_count = 5

"""
This True is actually represents as 1 and the False is represented as 0
This is also a short notation for it and to prove that this exists
i can show you this:
"""

# Sometime people does this, Here is_boiling is True and it is automatically converted to 1 and this is known as `upcasting`.
total_actions = str_count + is_boiling
print(f"Total actions: {total_actions}")

milk_present = 0  # no milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = False

can_sever = water_hot and tea_added
print(f"Can serve chai? {can_sever}")
