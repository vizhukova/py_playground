def func(name):
    print('Hi ' + name)

func("user")
func("Mike")

def cube(num):
   return  num * num * num

print(cube(3))

def return_the_biggest(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2
    
print("return_the_biggest:")    
print(return_the_biggest(2,6))

def return_in_between(val1, val2, val3):
    if val1 > val2 or val1 > val3:
        return  val1
    elif val2 > val1 or val2 > val1:
        return val2
    return val3

print("return_in_between:")  
print(return_in_between(3,2,1))
print(return_in_between(0,2,1))
print(return_in_between(3,2,4))

def return_the_biggest_in_3(val1, val2, val3):
    if val1 > val2 and val1 > val3:
        return  val1
    elif val2 > val1 and val2 > val1:
        return val2
    return val3

print("return_the_biggest_in_3:")
print(return_the_biggest_in_3(3,2,1))
print(return_the_biggest_in_3(0,2,1))
print(return_the_biggest_in_3(3,2,4))