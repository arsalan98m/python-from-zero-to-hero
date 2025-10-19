"""
Real-world style example: Invoice item

- Dataclass provides clear structure and behaviors
"""

from dataclasses import dataclass


@dataclass
class InvoiceItem:
    description: str
    unit_price: float
    quantity: int
    discount_percent: float = 0.0  # 0-100

    def total(self) -> float:
        subtotal = self.unit_price * self.quantity
        discount = subtotal * (self.discount_percent / 100.0)
        return round(subtotal - discount, 2)


items = [
    InvoiceItem("Chai - Masala", 2.5, 4),
    InvoiceItem("Chai - Ginger", 3.0, 2, discount_percent=10),
]

for it in items:
    print(it.description, "->", it.total())
