'''products = [
  {"name": "apple", "price": 1.00},
  {"name": "banana", "price": 0.50},
  {"name": "orange", "price": 0.75}
]

def add_taxes(i):
  item = i.copy()
  item["taxes"] = item["price"] * 0.12
  return item

products2 = list(map(add_taxes, products))

print(products)
print('Original list')
print(products2)
print('New list')
'''

n = 3
result = [ str(n) for n in range(1, n+1)]
print(result)