#UNIVERSAL TABLE:
#a*b = c
"""a = int(input("Enter a number: "))
b = 1
while b<=10:
    print(f"{a}X{b} = {a*b}")
    b+=1"""


#
"""number = int(input("enter a number :"))#1234
reversed_number = 0
original_number = number #1234

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

print(f"the reversed number of {original_number} is {reversed_number}" )

#
largest_number = None
while True:
  a = int(input("enter a number(enter 0 to stop) :"))
  if a == 0:
      break
  if largest_number is None or a > largest_number:
      largest_number = a

if largest_number is not None:
    print(f"the largest number entered is {largest_number}")
else:
    print("no numbers were entered ")
#

while True :
    word = input("enter a word: ")
    if word == "Python":
        break
    elif word != "Python":
        print("try again")
        word = input("enter a word: ")
        
print(f"the correct word is {word}") """   
#guessing game(1 to 100):
"""import random
secret_number = random.randint(1,100)
guess = int(input("enter a random number:"))
if guess > secret_number :
    print("too high!try again")
    guess = int(input("enter a random number:"))
elif guess < secret_number :
     print("too low!")
     guess = int(input("enter a random number:"))
else:
    print(f"congrats,the number is {secret_number}")
    break"""
   
#code 2 :
"""import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Enter a random number between 1 and 100: "))
    
    if guess > secret_number:
        print("Too high! Try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print(f"Congrats, the number is {secret_number}!")
        break"""

#
i = 1
while i<=10:
    print(i)
    i+=1
#
"""fruits = ["Mango","pineapple","Orange","apple"]
i = 0
while i<len(fruits):
    print(fruits[i])
    i+=1
objects = ("TV","Pen","Book","Laptop")
x = list(object)"""
numbers = [5,25,63,92,84]
print(numbers)
(a,b,c,d,e,) = numbers
print(a)
print(e)
numbers.remove(92)
print(numbers)
numbers.insert(1,"apple")
print(numbers)




