def my_decorator(func):
    def wrapper():
        print("Doing something before main function call")
        func()
        print("Doing something after main function call")
    return wrapper

@my_decorator
def main_function():
    print("Main function here")

main_function()