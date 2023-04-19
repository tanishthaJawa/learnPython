mydict = dict(name="Mary", age=28, city="Boston")
print(mydict)

value = mydict["name"]
print(value)

mydict["email"] = "abx@xyz.com"
print(mydict["email"])

del mydict["name"]
print(mydict)

mydict.pop('age')
print(mydict)

mydict.popitem()
print(mydict)

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["lastname"])
except KeyError:
    print("Invalid Data")

for key in mydict.keys():
    print(key)
for value in mydict.values():
    print(value)
for key, value in mydict.items():
    print(key, value)

mydict_cpy = mydict
print(mydict_cpy)  # refers to the same object

mydict2 = {"name": "Mary", "age": 28, "city": "Boston"}
mydict3 = {"name": "Mary", "age": 28, "city": "Ukraine", "email": "hi@ab.com"}
mydict2.update(mydict3)  # merges two dictionaries
print(mydict2)
print(mydict3)

mydict5 = {3: 9, 4: 16}
value = mydict5[3]
print(value)

mytuple = (8, 7)
mydict6 = {mytuple: 15}
print(mydict6)
