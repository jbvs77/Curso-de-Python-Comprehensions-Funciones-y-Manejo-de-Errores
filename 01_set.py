#set = conjuntos 
#{} ----> Lista
#[] -----> Diccionario
#() -----> Tupla 
#el conjunto no acepta duplicados


set_countries = {'col', 'mex', 'bol', 'mex'}

print(type(set_countries))
print(set_countries)


set_number = {1, 2, 2, 443, 23}
print(set_number)

set_types = {1, 'hola', False, 12.12}
print(set_types)


set_from_string = set('hola')
print(set_from_string)

numbers = (1, 2, 3, 1, 2, 3, 4)
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(type(unique_numbers ))