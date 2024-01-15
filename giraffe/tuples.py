coordinates = (4, 5)
print(coordinates)
print(coordinates[0])
print(coordinates[1])

# will cause the error as such index of an element does not existing in tuple
print(coordinates[5])
# will cause the error as tuples are immutable 
coordinates[0] = "new value"