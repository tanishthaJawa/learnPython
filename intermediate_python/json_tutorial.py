import json

mydict = {"name": "Mary", "age": 28, "city": "Boston", "hasChildren": False}

# Convert a python object to json as string
personJson = json.dumps(mydict, indent=4, sort_keys=True)
print(personJson)

# Convert a python object to json in a file
with open('person.json', 'w') as file:
    json.dump(mydict, file, indent=4)

# Convert a json object to python as string
person = json.loads(personJson)
print(person)

# Convert a json object to python in a file
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)


# Encode a custom object
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        return TypeError('Object of type User is not JSON serializable')


userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# Encode a custom object using json encoder
from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, o)


userJSON = json.dumps(user, cls=UserEncoder)
userJSON2 = UserEncoder().encode(user)
print(userJSON)


# Decoding
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON2, object_hook=decode_user)
print(type(user))
print(user.name)
print(user)
