#
"""list1 = [3,5,7,2,9]
maximum = max(list1)
minimum = min(list1)
print(f"The biggest number in the list is {maximum}")
print(f"the smallest number in the list is {minimum}")"""
#
def maximum_and_minimum(list1):
    maximum = max(list1)
    minimum = min(list1)
    return f"The biggest number is {maximum} and the smallest is {minimum}"
    

list1 = [3,5,7,2,9]
result = maximum_and_minimum(list1)
print(result)

#absolute value of a number:
x = 3 - 7.25
y = abs(x)
print(y)


#Create a class Car with attributes make, model, and year:
#Create an object of Car and print its attributes.
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

c1 = Car("Honda","City","2017")
print("Car:" + " " +c1.make)
print("model:" + " " +c1.model)
print("year:"+ " " +c1.year)

#Create a class Student with attributes name and age. Use the __init__ method to initialize these attributes.
#Create an object of Student and display the attributes.
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


S1 = Student("Ishaan",13)

print("name of student :" + " " + S1.name)
print("age of student :" , S1.age)

#Create a class Rectangle with attributes length and width.
#Create two different objects with different values and calculate their areas.

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length*self.width
             
R1 = Rectangle(28,12)
R2 = Rectangle(20,8)
print("Area of Rectangle: ", R1.calculate_area() )
print("Area of Rectangle2: ", R2.calculate_area())





    
