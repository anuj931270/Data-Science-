# Apply a 20% discount to a price
# Before: price = 1000
# After: ?

price_before =1000
discount_percent =20
discount_amount=price_before*(discount_percent/100)
price_after=price_before-discount_amount
print(f'Before price={price_before}')
print(f'After price={int(price_after)}')