from timeit import default_timer as timer

my_string = 'Hello World'
print(my_string)

my_string2 = """Hello
World"""
print(my_string2)

char = my_string[0]
print(char)
# my_string[0] = 'h'  # will produce error

# SLICING
substring = my_string[1:5]
print(substring)
substring = my_string[:5]
print(substring)
substring = my_string[::2]
print(substring)
substring = my_string[::-1]
print(substring)

name = "tom"
greeting = "Helli" + " " + name
print(greeting)

for i in name:
    print(i)

if 'hi' in name:
    print("Yes")

my_string = '       Hello World    '
my_string = my_string.strip()
print(my_string)
print(my_string.find('lo'))
print(my_string.replace('l', 's'))
print(my_string)

my_string = 'how are you doing'
my_list = my_string.split()
print(my_list)
new_string = ' '.join(my_list)
print(new_string)

my_list = ['a'] * 6
print(my_list)

my_string = ''
start = timer()
for i in my_list:
    my_string += i
stop = timer()
print(my_string)
print(stop - start)

# good
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)

# format strings
# %, format, f strings
var = "Tom"
my_string = "the variavle is %s" % var
print(my_string)

var = 3
my_string = "the variavle is %d" % var
print(my_string)

var = 3.2211
my_string = "the variavle is %.2f" % var
print(my_string)
my_string = "the variable is {}".format(var)
print(my_string)

var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2)
print(my_string)

var2 = 6
my_string = f"the variable is {var} and {var2}"
print(my_string)