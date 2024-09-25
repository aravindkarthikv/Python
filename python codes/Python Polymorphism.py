#
"""list1 = [3,5,7,2,9]
maximum = max(list1)
minimum = min(list1)
print(f"The biggest number in the list is {maximum}")
print(f"the smallest number in the list is {minimum}")"""
#
"""def maximum_and_minimum(list1):
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
print("Area of Rectangle2: ", R2.calculate_area())"""


#Write a program to print all even numbers from 1 to 50 using a for loop:

"""for x in range(1,51):
    if x%2 == 0:
        print(x)"""

#

"""for x in range(1,6):
    print("*"*x)"""
    
    
#10 times:
for x in range(1,11):
    print('*'*x)

#Take a string input from the user and count how many vowels are present in the string using a for loop:

'''string = input("Enter a String:")
vowel_count = 0

for char in string:
    if char in "aeiouAEIOU" :
        vowel_count+=1
        print(char)

print(f"no. of vowels - {vowel_count}")'''

#Take a character as input from the user and check whether it is a vowel or a consonant:

word = input("Enter a Letter:")
if len(word) == 1 and word.isalpha():
    if word in "aeiouAEIOU":
        print(f"{word} is a vowel")
    else:
        print(f"{word} is a consonant")

else:
    print("Invalid Input,Try again")

#
i = 1
while i<=50:
    print(i)
    i+=1
'''age = input("Enter your age: ")
if age == int:
    if age>=18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")

else:
    print("Invalid Input,enter your age in integers")'''

#Create a program that asks the user for a number and prints the multiplication table of that number using a while loop.
i = int(input("enter a number:"))
b = 1
while b<=10:
    product = i * b
    print(product)
    b+=1


