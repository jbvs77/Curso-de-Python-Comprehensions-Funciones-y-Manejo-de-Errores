products = [
    {"name": "apple", "price": 1.00},
    {"name": "banana", "price": 0.50},
    {"name": "orange", "price": 0.75}
]
print("Dict 1 ")
print(products)
print("")


def taxes(i):
  i['taxes'] = i['price'] * 0.12
  return
products2 = list(map(taxes, products))
print("Dict 1 ---- with map")
print(type(products2))
print("")
print("Dict 1 ")
print(products)
