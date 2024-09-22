myset = {"apple", 1, 3.5 ,"banana", "cherry","apple","cherry", True, "apple"}
print(type(myset))
print(len(myset))
print(myset)
myset.add("Orange")
print(myset)
Object = set(("Pen","Paper","Ball","Bat"))
print(Object)
print(type(Object))
(a,b,c,d)=Object
print(c)
#check wheather "Orange" is in the list:
print("Orange" in Object)
# print "Orange" which is not in the list:
print("Orange" not in Object)
#adding 2 sets:
Object.update(myset)
print(Object)
#adding a list to a set:
fruits = ["Orange","Mango","Lemon","Apple"]
Names = {"Aravind","Mohan","Sashwath","Ajay"}
Names.update(fruits)
print(Names)
#adding a tuple to a set:
mytuple = ("Tamil Nadu","Kerala","Karnataka","Gujurat")
newset = {"India","South Africa","USA","England"}
newset.update(mytuple)
print(newset)
#adding a tuple to a list:
newtuple = ("BMW","Toyota","Mercedes","Honda")
list1 = ["Banana","strawberry","Blueberry","Grapes"]
list1+=newtuple
print(list1)
# removing a value from a set:
#if a value is not there in a set discrad() will not show an error
Object.discard("Paper")
print(Object)
#pop() will randomly remove a value from a set
newset.pop()
print(newset)
#deleting a set:
#del myset
#clearing the values inside a set:
myset.clear()
print(myset)






