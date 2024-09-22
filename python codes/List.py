#List
x = "  My name is Aravind."
print(x)
print(x.casefold())
any_object = ["TV","Book","Apple","Pencil",'Battery',45,25.7,True]
print(len(any_object))
print(type(any_object))
print(any_object[4:])
#any_object[2]="Clock"
#any_object[4:]=[100,"pen",25.7,False]
print(any_object)
print(any_object[2:5])
fruits =["apple", "banana", "cherry", "apple", "cherry"]
fruits.append("Orange")
print(fruits)
fruits.insert(1,"orange")
print(fruits)
fruits2 =["Mango","Strawberry",]
fruits.extend(fruits2)
print(fruits)
fruits.remove("Strawberry")
print(fruits)
fruits.pop(3)
print(fruits)
#for loop
#for a in fruits:
 #   print(a)
for j in range(len(fruits)):
       print(j)
       print(fruits[j])
#while loop
i = 0
while i < len(any_object):
 print(i)
 i+=1
     
