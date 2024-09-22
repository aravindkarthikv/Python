#calculator:
"""num1 = int(input("Write a number: "))
num2 = int(input("Write a 2nd number: "))
addition = num1 + num2
multiplication = num1*num2
subtraction = num1-num2
division = num1//num2
Remainder = num1%num2
exponent = num1**num2
print("The Sum is: " + str(addition))
print("The product is: " + str(multiplication))
print("The Difference is: " + str(subtraction))
print("The quotient is: " + str(division))
print("The Remainder is: " + str(Remainder))
print("The exponent is: " + str(exponent))"""
fruits = ["orange","mango","apple"]
Objects = ["Laptop","Remote","Book","TV"]
Objects.append("Computer")
print(Objects)
fruits.insert(2,"Watermelon")
print(fruits)
Object2 = ["Phone","Bulb","Fan","Notebook"]
print(type(Object2))
#Objects.extend(Object2)
#print(Objects)
#Object2.clear()
#print(Object2)

#[ print(fruits[i]) for i in range(len(fruits))]

newObject2 = []
for x in Object2:
    if "b" in x:
        newObject2.append(x)
        
print(newObject2)

"""newfruitslist = []
for c in fruits:
    if "a" in c:
        newfruitslist.append(c)


print(newfruitslist)"""

newF = [x for x in fruits if "a" in x]
print(newF)


if "Phone" in Object2:
    print(True)
else:
    print(False)

    
sFruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
sFruits.sort()
print(sFruits)

iList=[699,29,89,4,60,12,458,]
iList.sort()
print(iList)










                      
