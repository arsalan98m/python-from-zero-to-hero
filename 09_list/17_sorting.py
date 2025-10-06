"""
Sorting in Python
=================

Sorting is the process of arranging elements in a specific order, typically ascending or descending.
Python provides two primary ways to sort data:

1. sort() Method:
-----------------
- Used with lists only.
- Modifies the original list (in-place sorting).
- Returns None.
- Supports optional arguments like:
  - `reverse=True`: for descending order.
  - `key=function`: for custom sorting logic.

2. sorted() Function:
---------------------
- Works with any iterable (lists, tuples, dictionaries, etc.).
- Returns a new sorted list; original data remains unchanged.
- Accepts the same optional arguments as `sort()`.

Use `sort()` when mutating the list is acceptable.
Use `sorted()` when you need to preserve the original data structure.

Sorting helps organize data for better readability, searching, and analysis.
"""
