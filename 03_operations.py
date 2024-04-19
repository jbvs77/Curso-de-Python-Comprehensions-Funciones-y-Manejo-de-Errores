set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#union 

set_c = set_a.union(set_b)
print(set_c)

#| = union 
set_c = set(set_a | set_b)
print(set_c)

#intersection --- toma solo los duplicados

set_c = set_a.intersection(set_b)
print(set_c)

#& = intersection
set_c = set_a.difference(set_b)
print(set_c )


#simetric difference --- une 2 conjuntos dejando duplicados fuera 

set_c = set_a.symmetric_difference(set_b)
print(set_c )