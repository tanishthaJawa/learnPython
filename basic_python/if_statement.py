is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male and tall ")
elif is_male and not is_tall:
    print("short male")
elif is_tall and not is_male:
    print("tall female")
else:
    print("You are  short female ")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


result = max_num(2, 5, 4)
print(result)
