# 📌 Example 1
def make_chai():

    return "Here is your masala chai"


print(make_chai())  # Here is your masala chai

# 📌 Example 2


def idle_chaiwala():
    pass


print(idle_chaiwala())  # None


# 📌 Example 3
def solid_cups():
    return 120


total = solid_cups()
print(total)  # 120


# 📌 Example 4
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"


print(chai_status(10))  # Chai is ready
print(chai_status(0))  # Sorry, chai over

# 📌 Example 5


def chai_report():
    return 100, 20, 30


report = chai_report()
print(report)  # (100, 20, 30) tuple
