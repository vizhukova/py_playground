from typing import Any, List, Union

class Student():
    dictionary = {
        "A+": 15,
        "A": 14,
        "A-": 13,
        "B+": 12,
        "B": 11,
        "B-": 10,
        "C+": 9,
        "C": 8,
        "C-": 7,
        "D+": 6,
        "D": 5,
        "D-": 4,
        "F+": 3,
        "F": 2,
        "F-": 1
    }
    MAX_VALUE = 15
    MIN_VALUE = 1

    def __new__(cls, *args, **kwargs):
        print('Performing custom actions here before the initialization')
        instance = super().__new__(cls)
        return instance

    def __init__(self, id: int, name: str, grades: List[str] = None):
        self.__dict__["_all_attr"] = {}
        self.id = id
        self.name = name
        self.grades = grades if grades is not None else []

    def __str__(self) -> str:
        return f"Student {self.name} with id {self.id}"
    
    def __len__(self) -> int:
        return len(self.grades)
    
    def __getitem__(self, index: int) -> Union[str, None]:
        if(index < len(self.grades) and index >= 0):
            return self.grades[index]
        return None
    
    def __setitem__(self, index: int, item: str):
        if(index < len(self.grades) and index >= 0):
            self.grades[index] = item

    def __setattr__(self, __name: str, __value: Any) -> None:
        if not __name.startswith("__"): self._all_attr[__name] = __value
        super().__setattr__(__name, __value)

    def print_all(self):
        for __name, __value in self._all_attr.items(): print(__name, __value)

    def __iter__(self):
        for i in range(0, len(self.grades)): yield self.name, self.grades[i]

    def __get_key_by_value__(self, search_value: int):
        for key, value in self.dictionary.items():
            if value == search_value:
                return key
        return None

    def __add__(self, other: int):
        def count_result(grade: str):
            nonlocal self
            result = self.dictionary[grade] + other
            if(result >= self.MAX_VALUE):
                return self.__get_key_by_value__(self.MAX_VALUE)
            return self.__get_key_by_value__(result)

        return map(count_result, self.grades)
    
    def __sub__(self, other: int):
        def count_result(grade: str):
            nonlocal self
            result = self.dictionary[grade] - other
            if(result <= self.MIN_VALUE):
                return self.__get_key_by_value__(self.MIN_VALUE)
            return self.__get_key_by_value__(result)

        return map(count_result, self.grades)
    
    def __del__(self):
        print(f"Destroying the instance of MyClass with name {self.name}")

    def __enter__(self):
        # for example make a database connection and return it (with with Student() as mydbconn:)
        print("Can be set up resources or perform any setup logic here")

    def __exit__(self, exc_type, exc_val, exc_tb):
       # The parameters exc_type, exc_value, and traceback allow handling exceptions that occurred within the 'with' block
        # for example make sure the dbconnection gets closed
       print("Can be performed cleanup or handle exceptions here")

student = Student(1, "Frank", ["A", "C+", "B"])
print("Student: ", student)
print("Length: ", len(student))
print("On index 1: ", student[1])
print("On index 3: ", student[3])
student[0] = "A-"
print("Changed 1st item: ", student[0])
student[5] = "С-"
print("Changed 1st item: ", student[5])
student.new_prop = 5
print("New property: ", student.new_prop)
student.print_all()
for name, grade in iter(student):
    print(name,grade)
print(list(student + 5))
print(list(student + 10))
print(list(student - 3))
print(list(student - 10))

# 
# Example of scopes and namespaces 
# 
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)