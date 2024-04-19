import random
'''countries = ['col', 'mex', 'bol', 'pe']

population_2 = {countries: random.randint(1, 100) for countries in countries}
print(population_2 )

result = {countries: population for (countries, population) in population_2.items() if population > 50}
print(result)'''

text = 'hola soy nicolas'
new_dict = {c: c.count() for c in text if c in 'aeiou'}
print(new_dict )