#Write a Python program to calculate the discount on a product based on its price:

#If the price is above $1000, give a 20% discount.
#If the price is between $500 and $1000, give a 10% discount.
#If the price is below $500, give a 5% discount.
def calculate_discount(price):
    discount_rate = 0
    if price>=1000:
        discount_rate = 0.20
    elif price>500 and price<1000:
        discount_rate = 0.10
    else :
        discount_rate = 0.05

    discount_amount = price*discount_rate
    final_amount = price - discount_amount
    return discount_amount, final_amount
#
price = float(input("Enter your price :$ "))
discount_amount, final_amount = calculate_discount(price)
print(f"the price is ${price:.2f}")
print(f"the discount is ${discount_amount:.2f}")
print(f"So,the final amount is ${final_amount:.2f}")

#code2:

"""def calculate_discount(price):
    discount_rate = 0
    if price >= 1000:
        discount_rate = 0.20
    elif price > 500 and price < 1000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05
    discount_amount = price * discount_rate
    final_amount = price - discount_amount
    return discount_amount, final_amount
price = float(input("Enter your price: $"))
discount_amount, final_amount = calculate_discount(price)
print(f"The price is ${price:.2f}")
print(f"the discount is ${discount_amount:.2f}")
print(f"So, the final amount is ${final_amount:.2f}")"""
