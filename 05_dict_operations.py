import random
'''dict = {}


for i in range(1, 11):
    dict[i] = i * 2
print(dict)


dict_v2 = {i: i*2 for i in range(1, 11)}
print(dict_v2 )
'''

'''countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)
print(population)

population_2 = {countries: random.randint(1, 100) for countries in countries}
print(population_2 )
             '''

names = ['nico', 'zule', 'santi']
age = [12, 56, 98]

'''for names, ages in zip(names, ages):
  print(names, ages)'''

personas = {names: age for (names, age) in zip(names, age)}

print(type(personas))

