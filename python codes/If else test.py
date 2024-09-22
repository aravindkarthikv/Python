#if else test:
#discount calculation:
"""def discount_calculation(price):
    discount_rate = 0
    if price>=1000:
        discount_rate = 0.20
    elif price>500 and price<1000:
        discount_rate = 0.10
    else :
        discount_rate = 0.05
    discount_amount = price * discount_rate
    final_amount = price - discount_amount
    return discount_amount, final_amount
price = float(input("What is the price of the purchase?: "))
discount_amount, final_amount = discount_calculation(price)

print(f"The price is ${price}")
print(f"The discount amount is ${discount_amount} ")
print(f"The Final price is ${final_amount}")"""

#password validation:
password = input("type a password: ")
lenght_criteria = False
upper_criteria = False
lower_criteria = False
numerical_criteria = False
if len(password)>=8:
    lenght_criteria = True
for char in password:
 if char.isupper():
    upper_criteria = True
 if char.islower():
     lower_criteria = True
 if char.isdigit():
    numerical_criteria = True
         
if lenght_criteria and upper_criteria and lower_criteria and numerical_criteria :
     print("The password is strong")
else:
     print("Invalid password")
    
#
n = int(input("enter a number: "))
sum1 = 0
i = 1
while i<= n:
    sum1+=i
    i+=1
print(f"the sum of the natural numbers upto {n} is {sum1}")


