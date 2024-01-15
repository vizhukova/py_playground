num1 = float(input("Enter a number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter another number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else: print("Error: Wrong operator")
    
    
print("Result: " + str(result))
