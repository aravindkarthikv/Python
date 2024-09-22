age  = 12
if age>=18:
    print("You are an Adult!")
else:
    print("You are a Minor")

temperature = 30
if temperature>30:
    print("It's a hot day")
else:
    print("The temperature is moderate")


score = 99
if score>=90:
    print("Grade A!")
elif score>=80:
    print("Grade B!")
else:
    print("Grade C!")

number = 1000
if number>0:
    print("the number is positive!")
elif number<0:
    print("the number is negative!")
else:
    print("The number is zero!")
    
days = 366
if days == 365:
    print("It is not a leap year")
elif days == 366:
    print("It's a leap year")

#check weather a specific year is a leap year:
"""year = int(input("Write a year:"))
if year%4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")"""
#HW:
"""score1 = int(input("What is Your Score?: "))
if score1>=90:
    print("grade A")
elif score1>80 and score1<89:
    print("grade B")
elif score1>70 and score1<79:
    print("Grade C")
elif score1>60 and score1<69:
    print("grade D")
else:
    print("Grade F(Fail)")"""
#even or odd number:
"""num1 = int(input("Write a number:"))
if num1%2 == 0:
    print(f"{num1} is a even number!")
else:
    print(f"{num1} is a Odd number!")"""

# vowel or consonant:
"""input_character = input("Write a character:")
if len(input_character) == 1 and input_character.isalpha():
    if input_character in "aeiou":
        print(f"{input_character} is a Vowel")
    else:
         print(f"{input_character} is a consonant ")
    

else:
    print("Invalid Input.Please give a Alphabet.")"""

#password Validation:

password = input("Type a Password:")
length_criteria = False
uppercase_criteria = False
lowercase_criteria = False
digit_criteria = False
special_criteria = False
if len(password)>=8:
    length_criteria = True
for char in password:
    if char.isupper():
        uppercase_criteria = True
    if char.islower():
        lowercase_criteria = True
    if char.isdigit():
        digit_criteria = True
    if char in "!@#$%^&*()":
        special_criteria = True
if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_criteria:
    print(f"{password} is a  valid Password!")
else:
     print(f"{password} is not a Valid Password")
     
if not length_criteria:
    print("Password needs to be 8 characters long")

#divisibility rule: 3 and 5
"""num1 = int(input("Write a Number:"))
if num1%3 == 0 and num1%5 == 0:
    print(f"{num1} is divisible by 3 and 5")
else:
    print(f"{num1} is not divisible by 3 and 5")"""

#Calculate Discount1:
"""price = float(input("What is the price?:"))
discount rate = 0
discount1 = price * discount rate

if price>=1000:
    discount rate = 0.20
    print(discount1)
elif price>500 and price<1000:
    discount rate = 0.10
    print(discount1)
else:
    discount rate = 0.05
    print(discount1)"""

# age group calculation:
"""age = int(input("what is your age?: "))
if age<=12:
    print("You are a Child!")
elif age>=13 and age<=19:
    print("You are a Teenager!")
elif age>=20 and age<=59:
    print("You are an Adult!")
else:
    print("Senior")

 #
    if age < 0:
    print("Invalid age")
    elif age <= 12:
    print("Child")
    elif age <= 19:
     print("Teenager")
    elif age <= 59:
    print("Adult")
    else:
     print("Senior")"""
#calculate discount2:
"""def calculate_discount(price):
    if price >= 1000:
        discount_rate = 0.20
    elif 500 <= price <= 1000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05
    
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    
    return discount_amount, final_price

# Example usage
price = float(input("Enter the price of the product: $"))

discount_amount, final_price = calculate_discount(price)

print(f"Original Price: ${price:.2f}")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Price after Discount: ${final_price:.2f}")"""

#temperature conversion:
"""def Celcius_to_Farenheit(Celcius):
    return (Celcius * 1.8) + 32
def Farenheit_to_Celcius(Farenheit):
    return (Farenheit - 32) / 1.8


temperature = float(input("Input the temperature : "))
unit = input("Enter the unit(C for Celcius ,F for Farenheit ):").strip().upper()
if unit == "C":
    converted_temp = Celcius_to_Farenheit(temperature)
    print(f"{temperature} C is equal to {converted_temp:.2f} F. ")
elif unit == "F":
    converted_temp = Farenheit_to_Celcius(temperature)
    print(f"{temperature} F is equal to {converted_temp:.2f} C.")
else:
    print("Invalid Unit!,Please enter C for Celcius or F for Farenheit")"""
    
    






     
     





















    


