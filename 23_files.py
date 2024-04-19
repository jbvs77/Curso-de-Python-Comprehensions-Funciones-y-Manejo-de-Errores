with open('./text.txt') as file:
  data = iter(file)
  try: 
    while True: 
      print(next(data))
  except StopIteration: 
    print('fin el archivo')


print('wenas')
  


  
#print(file.read())
'''
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
'''


'''
for line in file: 
  print(line)
file.close()
'''
