"""def my_function(fname,lname):
 print("Name: " + fname+ " " +lname)

my_function("Aravind","Karthik")

my_function("Aravind","Govind")


def name_function(child3,child2,child1):
    print("The youngest child is " + child3)
    print("The 2nd child is " + child2)
    print("The oldest child is " + child1)
    
name_function(child1 = "Rohan",child2 = "Aravind",child3 = "Mohan")"""
#Arbitery Arguments(* Args)
"""def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("A", "B", "C")

#Default Parameter Value:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function()

#Example 2:
def my_items(Item = "Pen"):
    print("I have a " + Item)

my_items("Remote")
my_items()
my_items("Phone")
my_items("Box")

#List as an argument:
fruits = ["apples","bananas","cheryys"]
def new_function(fruits):
    for x in fruits:
        print(x)

new_function(fruits)

#Returning a value:
def my_function(x):
  return 5 * x

print(my_function(3))"""

#Positional-Only Arguments:




#Arrays:
"""cars = ["Volvo","Ford","BMW"]
print(cars[0])
print(len(cars))
for x in cars:
    print(x)
cars.append("Honda")
print(cars)
cars.remove("Volvo")
print(cars)
cars.copy()
print(cars)

Num = [1, 4, 2, 9, 2,7, 8, 9,1, 3, 1,2]
print(Num.count(1))


#
Numbers = [0,1,2,3,4,5,6,7,8,9,10,8,9,1,0,9]
Numbers.append(11)
print(Numbers)
Numbers.copy()
print(Numbers)
print("Count of 9:",Numbers.count(9))
Numbers.extend(cars)
print(Numbers)
print("Index of Ford:",Numbers.index("Ford"))
Numbers.insert(17,"Lamborghini")
print(Numbers)
Numbers.pop(18)
print(Numbers)
Numbers.remove("Honda")
print(Numbers)
Numbers.reverse()
print(Numbers)

Num.sort(reverse = True)
print(Num)


Numbers.clear()
print(Numbers)"""

#

"""def sum_of_events(numbers):
  i = 0
  for x in numbers:
    if x%2 == 0:
      i = x + i
      print(i)
      
numbers = [1, 2, 3, 4, 5, 6]
result = sum_of_events(numbers)
print(result)

#code2:
def sum_of_events(numbers):
  return sum([x for x in numbers if x%2 == 0])

numbers = [1,2,3,4,5,6,]
results = sum_of_events(numbers)
print(results)
#
def sum_of_events(numbers):
  return sum([x for x in numbers if x%2 != 0])
numbers = [1,2,3,4,5,6,7,8,9,10]
result = sum_of_events(numbers)
print(result)


#maximum and minimum numbers in a list:
def new_function(numbers):
  maximum = max(numbers)
  minimum = min(numbers)
  return(minimum,maximum)

numbers = [45, 12, 78, 34, 89, 23]
result = new_function(numbers)
print(f"Minimum:{result[0]},Maximim:{result[1]}")

#
def count_occurrences(numbers,target):
  return numbers.count(target)

numbers = [1,4,7,1,5,11,2,3,1,6,5,7,0,12,1]
target = 4
result = count_occurrences(numbers,target)
print(f"Count of {target} = {result}")

#
def reverse_list(newlist):
  return newlist[::-1]

newlist = [1, 2, 3, 4, 5]
result = reverse_list(newlist)
print(f"the reversed order is {result}")

#
def remove_duplicates(newlist):
  uniquenew_list = []
  for num in newlist:
    if num not in uniquenew_list:
      uniquenew_list.append(num)
  return uniquenew_list


newlist = [1, 2, 2, 3, 4, 4, 5, 1]
result = remove_duplicates(newlist)
print(f"list after removing duplicates is {result}")"""

#
"""product = 1
list1 = [1, 2, 3, 4, 5]
for x in list1:
 product*=x

print(product)"""

def product_of_element(list1):
  product = 1
  for x in list1:
    product*=x
  return product
list1 = [1, 2, 3, 4, 5]
result = product_of_element(list1)
print(result)       

#
list1 = [3, 1, 4]
list2 = [2, 5, 6]
list1 = list1+list2
print(list1)
list1.sort()
print(list1)

#
def arranging_lists(list1,list2):
  list1 = list1+list2
  list1.sort()
  return list1

list1 = [3, 1, 4]
list2 = [2, 5, 6]

result = arranging_lists(list1,list2)
print(result)

#Lambdas:
y = lambda a:a + 10
print(y(7))

x = lambda a,b:a*b
print(x(7,10))

Z = lambda a, b, c : a + b + c
print(Z(300,24,18))

def my_function(n):
  return lambda a:a*n

doubler = my_function(2)
tripler = my_function(3)


print(doubler(25))
print(tripler(25))

#classes and objects:
#Create a class named MyClass, with a property named x:
class MyClass:
  x = 5
  
p1 = MyClass()
print(p1.x)

#
class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name} ,{self.age}"
    return f"My name is {self.name} and I am {self.age} years old"
            
p1 = Person("Aravind",12)

print(p1)



























