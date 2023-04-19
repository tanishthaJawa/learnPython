i = 1
while i <= 10:
    print(i)
    i += 1
print("loop ended")

friends = ["Jim", "karen"]
for letter in friends:
    print(letter)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])


def raise_to_power(base_num, pow_num):
    result = 1
    for j in range(pow_num):
        result = result * base_num

    return result


print(raise_to_power(2, 5))
