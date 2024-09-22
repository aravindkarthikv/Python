"""x =(5,10,15,20,25)
y = list(x)
(a,b,c,d,e) = y
print(a)
print(e)
y[1] = 12
print(y)
x = tuple(y)"""

#
"""coordinates = (3,4,5)
(x,y,z) = coordinates
print("x:",x)
print("y:",y)
print("z:",z)"""

#
"""word = {"e","d","u","c","a","t","i","o","n"}
vowels = {""}
for x in word:
    if x == "aeiou":
        vowels.add(x)
        print(vowels)"""
      
        
#code 2 :
#vowels_in_string = {char for char in "education" if char in 'aeiou'}
#print("Set of unique vowels from the string 'education':", vowels_in_string)       


#print numbers from 1 to 10:
x = 0
while x<=10:
    print(x)
    x+=1
#print even numbers from 1 to 10:
x = 0
