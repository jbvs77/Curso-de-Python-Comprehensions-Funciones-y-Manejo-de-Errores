path = './text.txt'
with open(path, 'w+') as file: 
  for line in file:
    print(line)
  for i in range(1,100):
    file.write(f'\nnueva shiet {i}')