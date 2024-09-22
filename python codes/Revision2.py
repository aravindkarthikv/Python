Names = ("Ishaan","Keshav","Avyukth","Aravind")
x = list(Names)
x.append("Mohan")
Names = tuple(x)
print(Names)
y = ("Kiran",)
Names+=y
print(Names)
#a = list(Names)
#a.remove("Keshav")
#Names = tuple(a)
#print(Names)
i = 0
while i<len(Names):
    print(Names[i])
    i+=1


tuple1 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(tuple1.index(7))
print(Names.index("Aravind"))
set1 = {"apple", 0, 289, False, "banana", "cherry", True, 1, 2}
print(set1)
set1.add("Pen")
print(set1)
set2 = {"Bat","Ball"}
set1.update(set2)
print(set1)
set1.pop()
print(set1)

