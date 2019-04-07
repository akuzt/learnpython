array1 = ['a', 'b', 'c']
array2 = array1[:]
# Если сделать просто присвоение, то ссылки будут на один объект! При изменениии первого объекта второй тоже изменится!
# array2 = array1
print(array2)
array1.append('d')
print(array1)
print(array2)
