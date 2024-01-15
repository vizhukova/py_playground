try:
    number = int(input("Enter the number: "))
    print("It's a number")
except ZeroDivisionError as err:
    print("Divide by zero" + err)
except ValueError:
    print("Invalid input")