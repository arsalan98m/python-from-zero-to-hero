"""
Real-World Example: E-Commerce System
=====================================

Complete example showing how dataclasses work together in a real application
"""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Enums for type safety


class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class PaymentMethod(Enum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"


# Product dataclass
@dataclass
class Product:
    product_id: int
    name: str
    description: str
    price: float
    category: str
    stock: int
    image_url: str
    rating: float = 0.0

    def is_available(self) -> bool:
        """Check if product is in stock"""
        return self.stock > 0

    def display(self):
        """Display product information"""
        availability = "✓ In Stock" if self.is_available() else "✗ Out of Stock"
        print(f"{self.name} - ${self.price:.2f}")
        print(f"  Category: {self.category}")
        print(f"  Rating: {self.rating}/5.0")
        print(f"  Stock: {self.stock} units - {availability}")


# Customer dataclass
@dataclass
class Customer:
    customer_id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    full_name: str = field(init=False)

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"

    def display(self):
        """Display customer information"""
        print(f"Customer: {self.full_name}")
        print(f"  Email: {self.email}")
        print(f"  Phone: {self.phone}")


# Shipping address
@dataclass
class Address:
    street: str
    city: str
    state: str
    zip_code: str
    country: str

    def format_address(self) -> str:
        """Format address as single string"""
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}, {self.country}"


# Order item (product + quantity)
@dataclass
class OrderItem:
    product: Product
    quantity: int

    def subtotal(self) -> float:
        """Calculate subtotal for this item"""
        return self.product.price * self.quantity

    def display(self):
        """Display order item"""
        print(
            f"  • {self.product.name} x{self.quantity} = ${self.subtotal():.2f}")


# Main Order dataclass
@dataclass
class Order:
    order_id: int
    customer: Customer
    items: List[OrderItem]
    shipping_address: Address
    payment_method: PaymentMethod
    status: OrderStatus = OrderStatus.PENDING
    tax_rate: float = 0.08
    shipping_cost: float = 10.00

    # Computed fields
    subtotal: float = field(init=False)
    tax: float = field(init=False)
    total: float = field(init=False)
    created_at: str = field(init=False)

    def __post_init__(self):
        """Calculate totals and set timestamp"""
        self.subtotal = sum(item.subtotal() for item in self.items)
        self.tax = self.subtotal * self.tax_rate
        self.total = self.subtotal + self.tax + self.shipping_cost
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update_status(self, new_status: OrderStatus):
        """Update order status"""
        self.status = new_status
        print(f"Order #{self.order_id} status updated to: {new_status.value}")

    def display_receipt(self):
        """Display full order receipt"""
        print("\n" + "="*60)
        print(f"ORDER RECEIPT - Order #{self.order_id}")
        print("="*60)
        print(f"Date: {self.created_at}")
        print(f"Status: {self.status.value.upper()}")
        print()

        print("CUSTOMER INFORMATION:")
        print(f"  Name: {self.customer.full_name}")
        print(f"  Email: {self.customer.email}")
        print()

        print("SHIPPING ADDRESS:")
        print(f"  {self.shipping_address.format_address()}")
        print()

        print("ORDER ITEMS:")
        for item in self.items:
            item.display()
        print()

        print("ORDER SUMMARY:")
        print(f"  Subtotal:      ${self.subtotal:>10.2f}")
        print(f"  Tax ({self.tax_rate*100}%):     ${self.tax:>10.2f}")
        print(f"  Shipping:      ${self.shipping_cost:>10.2f}")
        print(f"  " + "-"*25)
        print(f"  TOTAL:         ${self.total:>10.2f}")
        print()

        print(
            f"PAYMENT METHOD: {self.payment_method.value.replace('_', ' ').title()}")
        print("="*60 + "\n")


# Shopping Cart
@dataclass
class ShoppingCart:
    customer: Customer
    items: List[OrderItem] = field(default_factory=list)

    def add_item(self, product: Product, quantity: int = 1):
        """Add product to cart"""
        if not product.is_available():
            print(f"✗ {product.name} is out of stock!")
            return

        if quantity > product.stock:
            print(f"✗ Only {product.stock} units available!")
            return

        # Check if product already in cart
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                print(f"✓ Updated {product.name} quantity to {item.quantity}")
                return

        # Add new item
        self.items.append(OrderItem(product, quantity))
        print(f"✓ Added {product.name} x{quantity} to cart")

    def remove_item(self, product_id: int):
        """Remove product from cart"""
        self.items = [
            item for item in self.items if item.product.product_id != product_id]
        print(f"✓ Item removed from cart")

    def get_total(self) -> float:
        """Calculate cart total"""
        return sum(item.subtotal() for item in self.items)

    def display(self):
        """Display cart contents"""
        print("\n" + "="*60)
        print(f"SHOPPING CART - {self.customer.full_name}")
        print("="*60)

        if not self.items:
            print("Cart is empty")
        else:
            for item in self.items:
                item.display()
            print(f"\n  Cart Total: ${self.get_total():.2f}")

        print("="*60 + "\n")

    def checkout(self, shipping_address: Address, payment_method: PaymentMethod, order_id: int) -> Order:
        """Create order from cart"""
        if not self.items:
            raise ValueError("Cannot checkout with empty cart!")

        order = Order(
            order_id=order_id,
            customer=self.customer,
            items=self.items.copy(),
            shipping_address=shipping_address,
            payment_method=payment_method
        )

        # Clear cart after checkout
        self.items.clear()

        return order


# ============================================================================
# DEMONSTRATION
# ============================================================================

def main():
    print("\n" + "🛍️ " * 30)
    print("E-COMMERCE SYSTEM DEMO")
    print("🛍️ " * 30 + "\n")

    # Create products
    products = [
        Product(1, "MacBook Pro 16\"", "Powerful laptop for professionals",
                2499.99, "Electronics", 15, "macbook.jpg", 4.8),
        Product(2, "iPhone 15 Pro", "Latest smartphone with amazing features",
                999.99, "Electronics", 25, "iphone.jpg", 4.7),
        Product(3, "AirPods Pro", "Wireless earbuds with noise cancellation",
                249.99, "Electronics", 50, "airpods.jpg", 4.6),
        Product(4, "Magic Keyboard", "Wireless keyboard for Mac",
                99.99, "Accessories", 30, "keyboard.jpg", 4.5),
    ]

    print("AVAILABLE PRODUCTS:")
    print("-" * 60)
    for product in products:
        product.display()
        print()

    # Create customer
    customer = Customer(
        customer_id=12345,
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        phone="+1-555-0123"
    )

    print("\n" + "-"*60)
    customer.display()
    print("-"*60)

    # Create shopping cart
    cart = ShoppingCart(customer)

    # Add items to cart
    print("\nADDING ITEMS TO CART:")
    print("-" * 60)
    cart.add_item(products[0], 1)  # MacBook
    cart.add_item(products[2], 2)  # AirPods x2
    cart.add_item(products[3], 1)  # Keyboard

    # Display cart
    cart.display()

    # Create shipping address
    shipping_address = Address(
        street="123 Main Street, Apt 4B",
        city="New York",
        state="NY",
        zip_code="10001",
        country="USA"
    )

    # Checkout
    print("\nCHECKOUT:")
    print("-" * 60)
    order = cart.checkout(
        shipping_address=shipping_address,
        payment_method=PaymentMethod.CREDIT_CARD,
        order_id=1001
    )

    # Display receipt
    order.display_receipt()

    # Update order status
    print("ORDER PROCESSING:")
    print("-" * 60)
    order.update_status(OrderStatus.PROCESSING)
    order.update_status(OrderStatus.SHIPPED)
    order.update_status(OrderStatus.DELIVERED)
    print()

    # Display final receipt
    order.display_receipt()


if __name__ == "__main__":
    main()
