result = list(map(lambda n : n**2, [5,6,8,9,10]))
#print(result)

numbers = [1,2,3,4,5]
numbers2 = [6,7,8,9,10]

print(numbers)
print(numbers2)

numbers.extend(numbers2)

print(numbers)