# Example (Logical Operators)
age: int = 25
is_student: bool = True

# Check if age is greater than 18 AND is_student is True
if age > 18 and is_student:  # True
    print("You are eligible for a student discount.")

# Check if age is less than 12 OR greater than 60
if age < 12 or age > 60:  # False
    print("You qualify for a special discount.")

# Check if the person is NOT a student
if not is_student:  # False
    print("You are not a student.")
