mytuple = ("Max", 23, "Boston")
print(mytuple)

mytuple2 = "Max", 32
print(mytuple2)

mytuple3 = (32,)
print(type(mytuple3))

mytuple4 = tuple(["Max", 28, "Boston"])
print(mytuple4)

if "Tim" in mytuple:
    print("Yes")
else:
    print("No")

mytuple5 = ('a', 'p', 'p', 'l', 'e')
print(mytuple5.count('p'))
print(mytuple5.index('p'))

b = mytuple5[1:4]
print(b)

# list unpacking
name, age, city = mytuple
print(name)
print(age)
print(city)

i1, *i2, i3 = mytuple5
print(i1)
print(i2)
print(i3)
