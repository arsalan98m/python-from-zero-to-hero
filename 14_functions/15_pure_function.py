
"""
This is known as pure function because it doesn't have any side effects.
It doesn't alter any ingredient globally.
"""


def pure_chai(cups):
    return cups * 10


total_chai = 0

# ❌ not recommended way


def impure_chai(cups):
    global total_chai
    total_chai += cups
