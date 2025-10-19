"""
field() options: repr, compare, init, metadata

- Control which fields appear in __repr__
- Control which fields participate in comparisons (__eq__/ordering)
- Control if a field is set via __init__ (init=False)
- Provide metadata for tooling
"""

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Product:
    name: str
    price: float
    sku: str = field(repr=False, compare=False)
    # Derived field used for sorting; not passed in __init__
    sort_index: float = field(init=False, repr=False, compare=True)
    # Extra metadata that should not participate in comparisons
    metadata: Dict[str, Any] = field(default_factory=dict, compare=False)

    def __post_init__(self) -> None:
        self.sort_index = self.price


p1 = Product("Mug", 9.99, "SKU123", {"color": "white"})
p2 = Product("Mug", 9.99, "SKU999")

print(p1)                 # sku hidden from __repr__
print(p2)
print("p1 == p2:", p1 == p2)  # True (sku/metadata not compared)
