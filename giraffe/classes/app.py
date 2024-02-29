from student import Student

student1 = Student("Alex", 12, 1000)
student2 = Student("Vera", 15, 900)
print(student1)
print(student2)

student1.show()

# call class method using the class
Student.change_School('XYZ School')
# call class method using the object
student1.change_School('PQR School')

# call static method using the class
Student.find_notes('Math')
# call class method using the object
student1.find_notes('Math')

print(student1.name)
# returns error as param is private
# print(student1.__salary)
