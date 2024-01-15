for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Mike", "Jone"]
for friend in friends:
    print(friend)

for index in range(3, 10):
    print(index)    

for index in range(len(friends)):
    print(friends[index])

def raise_to_power (base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result
print(raise_to_power(3,3))
print(raise_to_power(2,8))

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1]
]
print(grid)
print(grid[1][2])

for row in grid:
   for col in row:
       print(col)

def magic_translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aoeiu":
            if letter.isupper(): 
                translation += "X"
            else: translation += "x"
        else: translation += letter
    return translation

print(magic_translator(input("Enter phrase: ")))

#comment one like
'''
multiple
line
comment
'''
