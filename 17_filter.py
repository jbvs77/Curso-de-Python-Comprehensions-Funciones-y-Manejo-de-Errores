number_list = [n for n in range(1, 100)]
even = list(filter(lambda n: n%2==0, number_list))

print(even)