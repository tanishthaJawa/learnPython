# list
# friends = ["Karen", "Suzie", "jeus", "ela"]
# print(friends[0])
# print(friends)
# print(friends[-1])
# print(friends[1:])
# print(friends[1:3])
# friends.extend(["lucky", "ruby"])
# print(friends)
# friends.append("rosy")
# print(friends)
# friends.insert(1, "teddy")
# print(friends)
# friends.remove("teddy")
# print(friends)
# print(friends.index('lucky'))
# print(friends.pop())
# print(friends.count('lucky'))
# friends.sort()
# print(friends)
# friends.reverse()
# print(friends)
# friends2c = friends.copy()
# print(friends2c)
# friends.clear()
# print(friends)
#
# #tuple
# coordinates = [(8, 10), (80, 3), (4, 5)]
# print(coordinates[0][0])

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][0])

for row in number_grid:
    print(row)
    for column in row:
        print(column)


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"
            translation += "g"
        else:
            translation += letter
    return translation


print(translate(input("Enter a phrase: ")))
