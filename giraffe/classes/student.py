class Student:
    '''documentation string'''

    # class variables
    school_name = 'ABC School'

    def __init__(self, name: str, age: int, salary: float):
        # instance variables
        self.name = name
        self.age = age
        # private member
        self.__salary = salary

    def show(self):
        print(self.name, self.age, Student.school_name)

    @classmethod
    def change_School(cls, name: str):
        cls.school_name = name

    @staticmethod
    def find_notes(subject_name: str) -> int:
        try:
            index = ['chapter 1', 'chapter 2', 'chapter 3', 'Math'].index(subject_name)
            print(f'Note {subject_name} is found on index {index}')
            return index
        except:
            print('No such note')
            return None