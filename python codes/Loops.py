Values = (1 ,True,"Mango",23.5,7,"Mango",1,23.5,True,"Mango")
print(Values)
x = list(Values)
x[1]="Banana"
Values = tuple(x)
print(Values)
fruits= ("apple", "banana", "cherry")
a = list(fruits)
a.append("Mango")
fruits = tuple(a)
print(fruits)
#how to add 2 tuples:
Objects=("Ball", "pen")
fruits+=Objects
print(fruits)
#how to remove a value in a tuple:
b = list(fruits)
b.remove("pen")
fruits = tuple(b)
print(fruits)
#how to remove a tuple:
#del fruits
#print(fruits)
#Unpacking a tuple:
cricket = ("Bat", "ball", "wicket")
(a,b,c)=cricket
print(a)
print(b)
print(c)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2 + cricket
print(tuple3)
y = cricket*2
print(y)


