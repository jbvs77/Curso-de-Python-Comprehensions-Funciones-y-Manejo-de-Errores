from pakete.modulo1 import func_1, func_2
from pakete.modulo2 import func_3, func_4
print(func_1())
print(func_2())
print(func_3())
print(func_4())



orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

def calculo(orders):
  total = 0
  for item in orders:
    total += item['total']
  return total

print(calculo(orders))