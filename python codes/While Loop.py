"""Objects = ["Apple","Laptop","Pen","Remote","Ball"]
i = 0
while i<len(Objects):
    print(Objects[i])
    i+=1
#
n = int(input("enter a number: "))
sum1 = 0
i = 1
while i<= n:
    sum1+=i
    i+=1
print(f"the sum of the natural numbers upto {n} is {sum1}")
#Write a Python program to display the multiplication table of a given number n. The program should display the table up to n
n = int(input("enter a number: "))
# n * b = c
b = 1
while b<=10:
    print(f"{n}X{b} = {n*b}")
    b+=1"""
#
"""n = int(input("enter a number: "))
i = 1
while i<=n:
    print(i)
    i+=1"""

#
"""n = int(input("enter a numebr: "))
i = 1
product = 1
while i<=n:
    product = product*i
    i+=1

print(product)"""""
#
correct_password = "Aravind_21_5_12"
password = input("Please enter your password: ")
while password != correct_password:
    print("incorrect password!,Try Again!!")
    password =  input("Enter the correct password:")
print("correct password!")

