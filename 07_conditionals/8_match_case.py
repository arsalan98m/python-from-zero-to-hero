"""
Python match-case Statement

Python introduced the match-case statement in Python 3.10 as a way to
implement structural pattern matching, which provides a cleaner and more 
readable alternative to traditional if-elif-else chains.
"""

# 1. Basic Syntax
# The match-case statement works by comparing an expression against multiple patterns. The syntax is:


def check_status(code):
    match code:
        case 200:
            print("OK")
        case 400:
            print("Bad Request")
        case 404:
            print("Not Found")
        case _:
            print("Unknown Status")


check_status(200)  # Output: OK
check_status(404)  # Output: Not Found
check_status(500)  # Output: Unknown Status
