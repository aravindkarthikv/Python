#python assignment operator
x=29
x+=5
print(x)
x-=10
print(x)
x*=6
print(x)
x/=12
print(x)
x%=5
print(x)
x**=3
print(x)
y=50
y//=6
print(y)
#List items are indexed, the first item has index [0],
# the second item has index [1]

myFriends=["John","Aravind","Ishaan","Jake","Ramu","Mohan","Ishaan"]
print(myFriends[1])
print(len(myFriends))
print(type(myFriends))
age=["11","12","12","13","11","10","12"]
print(age)
print(age[4])
print(len(age))
Values=list(("Mango",12,37.98,"Hello",True,False,))
print(Values)
print(Values[-5])
print(myFriends[1:7])
#printing all indexes from beggining to 4th place item,
#but excluding 5th place item Mohan
print(myFriends[:5])
#the values will include  5th item to  the end
print(myFriends[5:])
#if condition to find a item in a list
fruits=["apple","banana","cherry"]
if "banana" in fruits:
 print("Yes,Banana is in this List!")
if "kiwi" not in fruits:
 print("No.Kiwi is not in this List!")
print(myFriends[6])
print(myFriends[-1])
print(myFriends[5:])
myFriends[5]="Ram"
print(myFriends)
myFriends[3]="Mohan"
print(myFriends)
print(myFriends[2:5])
myFriends[2:5]=["Maya","Mohin","Advik"]
print(myFriends)
myFriends[2:1]="Keshav","Vihaan"
print(myFriends)
fruitsList=["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#fruitsList[1:2]="Pineapple","Strawberry"
#print(fruitsList)
fruitsList[1:3]=["Watermelon"]
print(fruitsList)
fruitsList.insert(5,"Strawberry")
print(fruitsList)
#Extend List : append elements from another list to the current list, use the extend() method.
Vegetables = ["Cabbage","Potato","Beetroot"]
fruitsList.extend(Vegetables)
print(fruitsList)
Vegetables.extend(fruitsList)
printVegetables)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
#Append Items : To add an item to the end of the list, use the append() method: 
thislist.append("orange")
print(thislist)                













