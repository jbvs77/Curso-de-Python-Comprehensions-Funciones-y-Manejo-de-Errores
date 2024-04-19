set_countries ={'col', 'mex', 'bol'}
#len() ---> tamanio del conjunto

print(len(set_countries))
#in ---> preguntar si un elemento esta dentro del conjunto
print('col' in set_countries)


#add ---> agregar un elemento al conjunto
set_countries.add('PE')
print(set_countries)

#update ---> actualizar un conjunto
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

#remove ---> eliminar un elemento del conjunto --- sino encuentra el elemento
#nos tira un error --- 

#seria mejor usar "discard" para evitar el error 
#set_countries.remove('ecua')
set_countries.discard('GTM')
print(set_countries)

#clear limpiara todo el conjunto
set_countries.clear()
print(len(set_countries))