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

# Factory:

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class Creator1(Creator):
    def factory_method(self) -> Product:
        return Product1()
    
class Creator2(Creator):
    def factory_method(self) -> Product:
        return Product2()
        
class Product1(Product):
    def operation(self) -> str:
        return "product 1"
    
class Product2(Product):
    def operation(self) -> str:
        return "product 2"
    
def client_code(creator: Creator) -> str:
    print('test')
    return creator.factory_method(super).operation()

result = client_code(Creator1)
print(result)
result = client_code(Creator2)
print(result)

# Decorator

def deco1(value): 
    def callback(func):
        def wrapper():
            print('Hello there' + str(value))
            func()
        return wrapper
    return callback

@deco1(1)
def test():
    print('my 1st try')

test()

# Singleton

class SingletonClass():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)

# Observer

class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(self, *args, **kwargs)

class Observer:
    def update(self, observable, *args, **kwargs):
        pass

class WeatherStation(Observable):
    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

class PhoneDisplay(Observer):
    def update(self, observable, *args, **kwargs):
        if isinstance(observable, WeatherStation):
            temperature = observable.temperature
            print(f"Temperature is {temperature} degrees Celsius")

weather_station = WeatherStation()
phone_display = PhoneDisplay()

weather_station.add_observer(phone_display)
weather_station.set_temperature(25)