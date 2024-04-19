'''import random
numbers = []

for e in range(1, 11):
    numbers.append(e)

print(numbers)'''

n = int(input("Ingrese un numero: "))
#for e in range(n):
#  print(e**2)


numbers = [ e**2 for e in range(n) if e % 2 != 0]
print(numbers)
