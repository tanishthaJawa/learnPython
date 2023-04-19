myList = ["banana", "cherry", "apple"]
print(myList)

mylist2 = list()
print(mylist2)

myList3 = [2, True, "Apple", "Apple"]
print(myList3)

item = myList[0]
print(item)

for i in myList:
    print(i)
if "banana" in myList:
    print("yes")
else:
    print("no")

print(len(myList))

myList.remove("cherry")
myList4 = [0] * 5
print(myList4)

myList5 = myList + myList4
print(myList5)

#slicing
a = myList5[1:3]
print(a)

a1 = myList5[::-1]
print(a1)

a2 = myList5[:]
print(a2)

myList6 = [1, 2, 3, 4, 5, 6]
b = [x + x for x in myList6]
print(b)
