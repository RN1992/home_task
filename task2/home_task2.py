# 3 переменные с одинаковыми идентификаторами.
dogs_name = 'Messi'
print(dogs_name)
print(id(dogs_name))

dogs_name2 = 'Messi'
print(dogs_name2)
print(id(dogs_name2))

dogs_name3 = 'Messi'
print(dogs_name3)
print(id(dogs_name3))

print()
print()

# 2 переменные с разными идентификаторами.

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))

print()
print()

# 3 переменные с разными идентификаторами

dogs_name = ['Messi']
print(dogs_name)
print(id(dogs_name))


dogs_name2 = ['Messi']
print(dogs_name2)
print(id(dogs_name2))

dogs_name3 = ['Messi']
print(dogs_name3)
print(id(dogs_name3))


print()
print()


# 2 переменные с одинаковыми идентификаторами

a = '1, 2, 3'
b = '1, 2, 3'
print(id(a))
print(id(b))
