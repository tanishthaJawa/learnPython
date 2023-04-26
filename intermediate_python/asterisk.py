# multiplication
a = 5 * 7
print(a)

# power
a = 5 ** 7
print(a)

# list ans string usage
mylist = [0, 1] * 10
print(list)

myList = (0, 1) * 10
print(list)

myList2 = "AB" * 10
print(list)


# function arguments
def foo(a, b, c, *args, **kwargs):
    print(a, b, c)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7)


# force only arguments
def boo(a, b, *, c):
    print(a, b, c)


boo(1, 2, c=3)

# unpacking arguments
myList = [2, 78.0, 9]
foo(*myList)

mydict = {'a': 2, 'b': 78.0, 'c': 9}
foo(**mydict)

# unpacking containers
numbers = [1, 2, 3, 4, 5, 6]
*beginning, last = numbers  # will always return a list
print(beginning)
print(last)

# merge iterables
my_tuple = (1, 42, 3)
myList = [4, 5, 6]
new_list = [*my_tuple, *myList]
print(new_list)

dica ={'a':1,'b':2}
dicb ={'c':3,'d':4}
dicT = {**dica,**dicb}
print(dicT)