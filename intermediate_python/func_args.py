def doo(a, b, c, d=4):
    print(a, b, c, d)


doo(1, 2, 3)

doo(b=1, a=2, c=3)
doo(1, b=2, c=3)


# variable arguments
def foo(a, b, c, *args, **kwargs):
    print(a, b,c)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7)


# force only arguments

def boo(a, b, *, c, d):
    print(a, b, c, d)


boo(1, 2, c=3, d=4)


def boo2(*args, d):
    for arg in args:
        print(arg)
    print(d)


boo2(1, 2, d=4)

# unpacking arguments

myList = [0, 1, 2]
doo(*myList)

mydict = {'a': 6, 'b': 8, 'c': 9}
doo(**mydict)

number = 0


def too():
    global number
    x = number
    number = 3
    print('number inside function', x)


too()
print(number)


# Call by object or call be object reference
def foo_x(t):
    t = 5


var = 10
foo_x(var)  # is an integer type which is immutable and can not be changed
print(var)  # 10


def foo_x(a_list):
    # a_list = [200, 400, 300] # won't change anything because we reassign reference(i.e. create a new local variable
    # named a_list that has nothing to do with global variable). The output would be :1,2,3 only
    a_list.append(4)  # mutable objects can be changed
    a_list[0] = 5  # immutable objects inside mutable containers can be changed


myList = [1, 2, 3]
foo_x(myList)
print(myList)
