tea_prices_pkr = {
    "Masala Chai": 100,
    "Green Tea": 120,
    "Elaichi Chai": 150,
    "Spicy Chai": 180,
}


tea_prices_usd = {
    tea: price / 80 for tea, price in tea_prices_pkr.items()
}

print(tea_prices_usd)
