"""
You're creating a monthly report for cafe's sales.
Instead of putting all logic on one place, break it down.

Task:
- Write a function `generate_report()` that calls:
  - fetch_sales()
  - filter_valid_orders()
  - summarize_data()
"""


def fetch_sales():
    print("Fetching the sales data...")


def filter_valid_orders():
    print("Filtering valid orders...")


def summarize_data():
    print("Summarizing the data...")


def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()
    print("Report generated successfully!")


generate_report()
