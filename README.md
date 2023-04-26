#Python

Python is interpreted, every line of code is executed in order.
To seperate a variable name we don't use camel case we use snake case i.e seperate it with an underscore(_)

# **Data Types:**
- String = ""
- Number : decimal or normal 
- Boolean = True,False

# **Common Functions:**
- input() - is used to input anything from user. By default python assumes everything you input is string.
- int() - convert a  string to a whole number
- float() - to a decimal number
- len() - is a function to get length
- str() - convert a number to string
- range() - defines a range from a number excluding the last number
- sorted()-sorts a data str. like list or anything without manipulating original list and returns a new list
-  print(my_num + "Hi") - will produce an error because my_num is of number and it can not be concatenated to string. Need to ocnvert that number to string. It prints everything on a new line. To print it on the same line use print(my_num,end=""). This will tell `print` statement to end its line without taking cursor to next line.

to import some math funtions, you need to have this line:
```
from math import *
and then use floor(3.8)

```


to get first character from a string avriable we use [] to acces it.
For example: 
```
name ="hila" # we can do name[0] to access h
```


## **List:**
is a data structure that allows us yo store ordered, mutable,duplicate and same/different  types of values. 

The syntax is :
```
friends = ["karen", True,2]
```


Forward indexing starts from 0 and backward indexing starts from -1. 
You can also specify a range 
for ex: 
```
friends[1:3] # this will get all elemnets after index 1 excluding 3 index
```


### Common Functions:
- insert(index, item) - adds an item at specific index
- append(item)- adds an item to last of the index
- pop() - removes an item from last
- len()- to find the size of list
- remove(item)- removes the particular item. If item not found, it gives a value error
- clear() - removes all element
- sort()- sorts a list
- list() - creates a list based on the argument. If no argument present creates an empty list.

### Examples:

```

myList4 = [0] * 5  
print(myList4)   # will contain 4 0's
  
myList5 = myList + myList4  
print(myList5)  # combines both lists

a = myList5[1:3]  # this is called as slicing
print(a)  # print elements from index 1 upto 2(last index is enclusive)

a2 = myList5[:]  
print(a2) # will create another list
  
a1 = myList5[::-1]  - this :: -1 is a step over. It could be any value. This mean get the next value. 
print(a1) # this will print reversed list

myList6 = [1, 2, 3, 4, 5, 6]  
b = [x + x for x in myList6]  
print(b) # will print [2, 4, 6, 8, 10, 12] i.e for each element it will perform an operation 1+1 =2, 2+2=4 etc.

```


# **Tuple:**
is an ordered data structure that allows us to store values which can not be changed. They are immutable. Generally used to store data that need not to be changed. Tuples are faster and more efficient than lists. To store the same amount of data a tuple would be a wiser choice if a data set is quite large.

Forward indexing starts from 0 and backward indexing starts from -1.

The syntax is:
```
coordiantes =(8,10) 
mytuple2 = "Max", 32  # the brackets are optional
```

- tuple(iterable_data_str): will create a tuple for you
- If you put a single element inside a tuple it will not recognise it as a tuple, inside. it will recognise it as a string or an int or whatever, and thus you need to do this for it to be recognised as a tuple: 
```
mytuple3 = (32,)  # put a comma at the end
```


### Common Functions:
- count(element) - counts the occurance of an elemnent in tuple.
- index(element) - finds the index of an element

You can easily convert a list to tuple and vice versa using list(tuple_name) and tuple(list_name) respectively.
to access it : coordinates[0] will give 8

### Examples
```
a = myTuple5[1:3]  # this is called as slicing
print(a)  # print elements from index 1 upto 2(last index is enclusive). If you don't specify starting index it will staart from 0 and similary for end index as well

a2 = myTuple5[:]  
print(a2) # will create another tuple
  
a1 = myTuple[::-1]  - this :: -1 is a step over. It could be any value. This mean get the next value. 
print(a1) # this will print reversed tuple

mytuple = ("Max", 23, "Boston")
name, age, city = mytuple  # called as list unpacking
print(name)  # Max
print(age)  #28
print(city)  # Boston

mytuple5 = ('a', 'p', 'p', 'l', 'e')  
i1, * i2, i3 = mytuple5   # called as list unpacking
print(i1) # a
print(i2)  #['p', 'p', 'l'] : is a list containing leftover elements
print(i3) # e

```


# **Dictionary:**
- is an unordered and mutable data structure that allows us to store data in the form of keys and values . 

- The syntax is: 
```
monthConversions = {  
    "jan": "January",  
    "feb": "February",  
    "mar": "march"  
}  
print(monthConversions["feb"])  
print(monthConversions.get("roy", 1))

mydict = dict(name="Mary", age=28, city="Boston")  
print(mydict)

- You can access and mutate elements like this:
value = mydict["name"]  
print(value)  
  
mydict["email"] = "abx@xyz.com"  
print(mydict["email"])

or just use mydict[indexValue]

```


### Common Functions:
- pop(key_name) - removes a key value pair of given key name
- popitem() - rmeoves last inserted key value pair
- keys - returns a list of keys
- values - returns a list of values
- items - returns both key and value
- update - merges two dictionaries and update them
- get(keyname,default value) - gets a value for the keyname and allows you to specify a default value

The keys can only be of immutable types. If using a number as a key, ensure that you never access the dictionary using the index value then.  

For example:
```
mydict5 = {3: 9, 4: 16}  
value = mydict5[3]  
print(value)

```


You can also use a tuple as a key but do not use a list as a key because they are of mutable types. For example:
```
mytuple = (8, 7)  
mydict6 = {mytuple: 15}  
print(mydict6)
```


### Examples:
```
del mydict["name"]  # default del method
print(mydict)  
  
mydict.pop('age')  
print(mydict)  
  
mydict.popitem()  # removes last item
print(mydict)

```


#### Iteration
```
for key in mydict.keys():  
    print(key)  
for value in mydict.values():  
    print(value)  
for key, value in mydict.items():  
    print(key, value)

mydict2 = {"name": "Mary", "age": 28, "city": "Boston"}  
mydict3 = {"name": "Mary", "age": 28, "city": "Ukraine", "email": "hi@ab.com"}  
mydict2.update(mydict3) # merges two dictionaries  
print(mydict2)  
print(mydict3)

```


You can make a comment using # and multiple lines comment using ''' three quotes

# Sets
- is an unordered and mutable data structure that allows us to store data but unlike lists and tuples do not allow duplicate elements.
- The syntax is :
```
myset ={1,2,3}
or 
myset2 = set(iterable)

```


### Common Functions:
- add(element) - add an element
- remove(element) - remove an element, produces an error if element does not exit
- discard() - removes an element and does not produce an error if element does not exist
- clear()- empties the set
- pop() - removes an arbitrary element from set and returns it
- union(set_name) - unions a setA on which union is invoked and returns a new set holding values inunion with second set
- intersect(setB) - intersects a setA on which intersection is invoked and returns a new set holding values in intersection with second set
- diff(setB) -   returns a new set holding values in difference with second set
- symmetric_difference(SetB) - returns a new set containing  all the values except those that are not in both sets
- update(setB) - it updates the existing set comabinig all tye values in setA and setB
- intersection_update(setB) - updates setA(invoking set) with only values that are common in both A and B
- difference_update(setB) - updates setA with all the values that are in A but not in B
-   symmetric_difference_update(setb) - updates setA containing  all the values except those that are not in both sets
- issubset(set) - returns a boolean indicating if a set is a subset of another set
- issuperset(Set) - returns a boolean indicating if a set is a superset of another set
- isdisjoint(Set) - returns a boolean indicating if a set is a disjoint (have no common elements ) of another set

- frozenset is also a collection data type that allows us to store elemnets and is an immutable version of set.
- For example : 
```
a = frozenset([1, 2, 3, 4])
```

- adding, removing or any other operations will produce an error if done on frozenset.

# Strings
- is an ordered, immutable collection data type that is used for text representation. It is the msot commonly used datatype.
- Syntax:
- Can use a single quote or double quote,single quote is more common though

```
my_string = 'Hello World'  
print(my_string)  
  
my_string2 = """Hello  # Triple string used for string to run on new line
World"""  
print(my_string2)
- Can access elements like this:
char = my_string[0]  
print(char)

```
    
You can also use negative index to get elements from last

### Common Functions:
- strip() - removes the white space from a string but does alter the original string in place and thus you have to manually reassign it.
- upper() - converts a string to upercase
- lower() - converts a string to lowercase
- startswith(string) - check if a string starts with a given string
- endswith(string) - check if a string ends with a given string
- find(string) - finds the index for a given string in another string. If the given string does not exist it returns -1
- replace(oldstr,newstr) - returns a new string which replaces old string with new string and does not modify existing string
- split() - splits a string to a list. The default argument is a space(" ") but you can put a comma or whatever
- join() - joins one string to another

#### format strings  :
- #### Three methods:
     - ###### %: - old formatting style.
 Example:
 ```
 var = "Tom"  
 my_string = "the variavle is %s" % var  
 print(my_string)  
  
var = 3  
my_string = "the variavle is %d" % var  
print(my_string)  
  
var = 3.2211  
 
```
 
my_string = "the variavle is %.2f" % var  # here %.2f indicates that it is floating point and we want only two digits after decimal. You can use %f as well
print(my_string)
     - format, 
     - f strings 
 
```
var = "Tom"  
my_string = "the variavle is %s" % var  
print(my_string)  
  
var = 3  
my_string = "the variavle is %d" % var  
print(my_string)  
  
var = 3.2211  
my_string = "the variavle is %.2f" % var  
print(my_string)

- ###### format() - method - also old way
my_string = "the variable is {}".format(var)  
print(my_string)  
  
var2 = 6  
my_string = "the variable is {:.2f} and {}".format(var, var2)  
print(my_string)

```

- ###### f strings
```
var2 = 6  
my_string = f "the variable is {2*var} and {var2}"  # evaluates variable values in run time
print(my_string)

```



### Examples:
```
my_string[0] = 'h'  # will produce error because string is immutable

substring = my_string[1:5]   # Slicing works just like it works in any other data structure
print(substring)

my_string = '       Hello World    '  
my_string = my_string.strip() # removes white space

my_string = 'how are you doing'  
my_list = my_string.split()  
print(my_list)  
new_string = ' '.join(my_list)  
print(new_string) # converts a list to string by joining 

##### performance bad 
my_string = ''  
start = timer()  
for i in my_list:  
    my_string += i  
stop = timer()  
print(my_string)  
print(stop - start)  
  
##### good  practice
start = timer()  
my_string = ''.join(my_list)  
stop = timer()  
print(stop - start)

```



# Function syntax:
```
def function_name():
       print("say Hi")

function_name()
```

## function arguments

- ### Keyword arguments: Order does not matter
```
def doo(a, b, c):  
    print(a, b, c)  
  
  
doo(a=1, c=2, b=3) # order does not matter

```

- ### Positional arguments:
```
def doo(a, b, c):  
    print(a, b, c)  
  
  
doo(1, 2, 3)

```

- ### Mix of both
```
doo(1, b=2, c=3) # should first use postional and then keyword and do not try to assign same argument twice.
```

- ### Default arguments: should be always at the end
```
def doo(a, b, c, d=4):  
    print(a, b, c, d)  
  
  
doo(1, 2, 3)

```

- ## variable length arguments:
 ```
 def foo(a, b, c, *args, **kwargs):  
    print(a, b)  
    for arg in args:  
        print(arg)  
    for key in kwargs:  
        print(key, kwargs[key])  
  
  
foo(1, 2, 3, 4, 5, six=6, seven=7)

```

- You can specify variable length arguments using  (*args) or (**kwargs)
- Although the name could be anything you generally use args and kwargs with * and **.
- * args refer to any no. of psoitional arguments. It is of tuple type
- * *kwargs refer to any no. of keyword arguments. It is of dictioanry type

## force only arguments  
- if you want to force your fucntion to have keyword agruments you can either use a * and a *args parameter which also forces to have a keyword argument

```
def boo(a, b, *, c, d):  
    print(a, b, c, d)  
  
  
boo(1, 2, c=3, d=4)  
  
  
def boo2(*args, d):  
    for arg in args:  
        print(arg)  
    print(d)  
  
  
boo2(1, 2, d=4)
```

## Unpacking function arguments
```
def doo(a, b, c, d=4):  
    print(a, b, c, d)
    
myList = [0, 1, 2]  
doo(*myList)  
  
mydict = {'a': 6, 'b': 8, 'c': 9}  
doo(**mydict)

```

- The arguments can be unpacked from a list or tuple but the length of list or tuple should be same as length of function arguments
- The arguments can be unpacked from a dictioanry but the length of dictioanry should be same as length of function arguments and the name of keys should be same as the parameter name

## Gloabl variable:

```
def too():  
    x = number  
    number=3  # This will produce an error you can not modify a glibal variable directly as this will create a new variable locally
    print('number inside function', x)  
  
  
too()

def too():  
    global number  
    x = number  
    number = 3  
    print('number inside function', x)  
  
  
too()  
print(number)

```


# Call by object and Call by object reference
```
# Call by object or call be object reference  
def foo_x(t):  
    t = 5  
  
  
var = 10  
foo_x(var)  # is an integer type which is immutable and can not be changed  
print(var)  # 10  
  
  
def foo_x(a_list):  
    # a_list = [200, 400, 300] # won't change anything 
     a_list.append(4)  # mutable objects can be changed  
    a_list[0] = 5  # immutable objects inside mutable containers can be changed  
  
  
myList = [1, 2, 3]  
foo_x(myList)  
print(myList)
```

- immutable types can not be changed
- mutable types can not be changed
- immutable objects inside mutable can be changed
- when  we reassign reference(i.e. it creates a new local variable internally named a_list that has nothing to do with global variable inside above code )mutable types are not changed. The output would be :1,2,3 only

# if else syntax:
```
if is_male and is_tall:  
    print("You are a male and tall ")  
elif is_male and not is_tall:  
    print("short male")  
elif is_tall and not is_male:  
    print("tall female")  
else:  
    print("You are  short female ")
```


# Loops:
```
i = 1  
while i <= 10:  
    print(i)  
    i += 1  
print("loop ended")  
  
friends = ["Jim", "karen"]  
for letter in friends:  
    print(letter)
    
```



# Collections
The collections module implements special container types that provide us with some additional functionality. Five types of them:
- ## Counter:
    - is a data str. that store elements as dictionary keys and their count as values 
    - ### Common functions:
    - items() - gives you a iterable of keys and values that are presnet
    - keys() - gives a iterable of keys
    - values() - gives a iterable of values
    - most_common(n) - gives a list cointaining tuples of most common n items with the element and value
- ### Example:


```
 from collections import Counter  

1a = "aaaaaaaabbbbcccc"  
my_counter = Counter(a)  
print(my_counter)  
print(my_counter.items())  
print(my_counter.keys())  
print(my_counter.values())  
print(my_counter.most_common(2))  
print(my_counter.most_common(1)[0][0])  # get first element of first tuple(most common element)  
print(list(my_counter.elements()))
```

- ## Named Tuple:
   - As the name suggests it is a  tuple with a name.
   - ### Example:
```
 from collections import namedtuple  

Point = namedtuple('Point','x,y')  
pt = Point(1,-4)  
print(pt)  
print(pt.x,pt.y)

```

What it does is taht it creates a class with any name here it is point. And the first argument of namedTuple is genrally the same name of class along with taht you specify the no. of fields that you want in your class. You can acces these members from the pt variable because it is of Point type.

- ## OrderedDict
- is like a normal dictionary except it remembers the order. Since python 3.7 dictioanries also remember order, so this is old school now.
- ### Example:
```
from collections import OrderedDict

ordered_dict = OrderedDict()  
ordered_dict['a'] = 1  
ordered_dict['d'] = 2  
ordered_dict['c'] = 3  
ordered_dict['b'] = 4  
print(ordered_dict)

```

- ## DefaultDict
- is like a normal dictionary except it remembers the order except it provides a default value if a key does not exist.
- We can specify the default type we want and python will automatically provide us the default value of default type
- ### Example:
```
d = defaultdict(int)  
d['a'] = 1  
d['b'] = 2  
print(d['c'])

```

- ## deque
-  is a double ended queue
- ### Common Functions:
   - append(item) - adds an item
   - popleft() - removes an item from front
   - pop() - removes element from the end
   - appendleft(item) - allows elements to be inserted on the left side i.e in the front 
   - extend(iterable) - allows us to extend our queue and add more elements
   - extendleft(iterable) - allows us to extend our queue and add more elements in front
   - rotate(num) - rotates the queue by num.

```
de = deque()  
de.append(1)  
de.append(2)  
de.appendleft(3)  
print(de)  
  
de.pop()  
print(de)  
  
de.popleft()  # allows elements to be removed on the left side i.e in the front side
print(de)  
  
de.extend([4,5,6])  # allows us to extend our queue
print(de)  
  
de.extendleft([4,5,6])  
print(de) # output will be 6,5,4 because we first insert 4, then 5, then 6. thus 6 is on the front side
  
de.rotate(1)  
print(de)  
  
de.rotate(-1)  
print(de)  # reverses the queue
  
de.rotate(2)  
print(de)
```



# Reading/ Writing/Appending Files: 
- use open command with the file name/path and modes could be :
    - r : read
    - r+ - read and write
    - w - write
    - a - append /only add data
- use close command to close it
- isreadable() - check if file can be read
- readLine() - read a line
- readlines() - read every single line, but if you do readline before it might not read it.
- write() - will write new text. If used with append tag will append at the end. If used with write it will overwrite
- append can mess up the file if you run it twice.

Ex:
```
employee_file = open("employees.txt", "r")  
 print(employee_file.readline())  
 print(employee_file.readline())  
 print(employee_file.readlines()[1])  
  
for employee in employee_file.readlines():  
    print(employee)  
  
    employee_file.close()
```


# Modules
- These are essentially useful files conatining useful functions that you would like to import in your code.
They are of three types:
- Built in : already available in python
- External modules : in lib folder of external libraries
- External third party modules : found in site - package
- The syntax is :

```
import  filename
print(filename.methodName())
```

- The pip is a package manager to install different modules

# IterTools
- is a module containing collections of tools for handling iterators
- Types of them:

## Product:
- is a function that gives a cartesian product for each element
- For example:

```
from itertools import product
  
a = [1, 2]  
b = [3]  
prod = product(a, b, repeat=2)  #the second is an optional argument specifies no of times to repeat the element
print(list(prod)) # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

```


## Permutations: 
- is a fucntion that gives permutations for an iterable.
- For example:
```
from itertools import permutations 

a = [1, 2, 3]  
perm = permutations(a,2)  # second optional argument specify the permutations
print(list(perm)) # will give [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

```


## Combinations:
- is a function that gives combinations for an iterable
- For example:
```

from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]  
comb = combinations(a, 2)  

print(list(comb))  #[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

comb_Wr = combinations_with_replacement(a,2)

print(list(comb_Wr)) #[(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

```


## Accumulator
- is a function used to perform some binary operation, by default adds all elements of the list
- Example:
```
from itertools import accumulate  
import operator

acc = accumulate(a)  
print(a)  
print(list(acc))  # [1, 2, 3, 4]

  
acc = accumulate(a, func=operator.mul)  
print(a)  
print(list(acc)) # [1, 2, 6, 24]

```


## GroupBy
- is a function used to group values based on keys

```

from itertools import groupby

def smaller_than_3(input):  
    return input < 3  
  
  
group_obj = groupby(a, key=smaller_than_3)  
for key,value in group_obj:  
    print(key,list(value)) 
    # True [1, 2]
    #False [3, 4]

```

## Infinite functions
- ### Count:
   - is a function that used to count infinitely.
   Example:

```
from itertools import count

for i in count(10):  
    print(i)  
    if i == 15:  
        break

```

- ### Repeat
   - is a function used to repeat a starting value as many times as you want
   - The second argument is for no. of times you want to repeat
   - Example:

```
from itertools import repeat

for i in repeat(1,4):  
    print(i)
    
```


- ### Cycle
  - is used to cycle through a list infinitely
  - Example:

```
from itertools import cycle

a = [1,2,3]  
for i in cycle(a):  
   print(i)

```







# Classes
```
class Student:  
  
    def __init__(self, name, major, gpa, is_on_probation):  
        self.name = name  
        self.major = major  
        self.gpa = gpa  
        self.is_on_probation = is_on_probation  
  
  
student1 = Student("nia", "science", 4.9, True)  
print(student1.name)

```


To import in another file we would write it as
from Student import Student 
meaning from student file import student datat type

# inheritance
Syntax:
```

from parent import parent
child_class(Parent class)

```



# Lambdas
- are anonymous one line functions. Used in higher order functions or just as one liners
- Syntax:
```
lambda arguments: operation
```
- Four most common functions:-
    - sorted(iterable, key) - sorts an iterable. Here key could be a function name or a lambda 
    - filter(func,seq) - first argument is a boolean condition(lambda or function) and second is iterable
    - map(func,seq) - is used to map to different map object. first argument is a function that takes a lambda or function and second is iterable
    - reduce(func,seq) - is used to perform some operation on every element and return a single value.

```

from functools import reduce  
  
add10 = lambda x: x + 10  #avoid assigning a lambda to a variable
print(add10(5))  
  
mult = lambda x, y: x * y  
print(mult(2, 7))  
  
points2D = [(1, 2), (15, 1), (5, -1)]  
points2D_sorted = sorted(points2D, key=lambda x: x[1])  # sorts by y index  
print(points2D)  
print(points2D_sorted)  
  
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])  # sorts by sum 
  
print(points2D_sorted)  
  
# map(func,seq)  
a = [1, 2, 3, 4, 5]  
b = map(lambda x: x * 2, a)  
print(list(b))  
  
# filter(func,seq)  
b = filter(lambda x: x % 2 == 0, a)  
print(list(b))  
  
# list comprehension  
c = [x for x in a if x % 2 == 0]  
print(c)  
  
# reduce(func,seq)  
product_a = reduce(lambda x, y: x * y, a)  
print(product_a)

```

# Exceptions
- Python programs terminate as soon as there is an error whether it is syntactic or an eexception
- ## Types of error:
         - TypeError
         - ImportError
         - NameError
         - FileNotFoundError
         - ValueError
         - IndexError
         - KeyError

```
# a = 5 + 's'  # TypeError  
# import somemodule #import error  
# a = 5  
# b = c #NameError : c not defined
# f = open('somefile.txt') #file not found error  
# a = [1, 2, 3]  
# a.remove(4) #ValueError  
# a[4] #IndexError  
# my_dict = {'name': 'Max'}  
# age = my_dict['age'] #KeyError : key not found

```

- ## Ways of throwing an exception:
    - ### Using assert :
```
x = -5  
assert (x >= 0, 'x is not positive') #Assertion Error

```
- ### Using raise:
```
 if x < 0:  
     raise Exception('x should be positive')

```

- ## Ways of handling an exception:
     #### Try syntax:
```
try:  
    value = 10 / 0  
    num = int(input("Enter a number"))  
    print(num)  
except ZeroDivisionError as err:  
    print(err)  
except ValueError:  
    print("Invalid Value")
    
```

```
try:  
    a = 5 / 1  
    b = a + 10  
  
except ZeroDivisionError as err:  
    print(err)  
except TypeError as err:  
    print(err)  
else:  # will get printed if no exception occurs
    print('everything is fine')  
finally:  # will execute even if exception is not raised
    print("cleaning up")

```

- ## Defining custom Exceptions:
  - By extending the exception class:
```
class ValueTooHighError(Exception):  
    pass  #class with no methids yet 
  
  
class ValueTooSmallError(Exception):  
    def __init__(self, message, value):  
        self.message = message  
        self.value = value  
  
  
def test_value(x):  
    if x > 100:  
        raise ValueTooHighError('value is too high')  
    if x < 5:  
        raise ValueTooSmallError('value is too small',x)  
  
  
try:  
    test_value(1)  
except ValueTooHighError as e:  
    print(e)  
except ValueTooSmallError as e:  
    print(e.message, e.value)

```

pass is a null operation — when it is executed, nothing happens. It is useful as a placeholder when a statement is required syntactically, but no code needs to be executed, for example:
def f(arg): pass    # a function that does nothing (yet)

class C: pass       # a class with no methods (yet)

# Logging
- Python has built in logging module 
- We call it as root logging module that can be used in root file
- By default a logger logs only message of warning, info and critical
- You can use basic config method  to add configuration options

```
import logging  
  
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
                    datefmt='%m/%d/%Y %H:%M:%S')  
  
import intermediate_python.loggingHelper  
  
logging.debug("A DEBUG Message")  
logging.info("An INFO")  
logging.warning("A WARNING")  
logging.error("An ERROR")  
logging.critical("A message of CRITICAL severity")

```

- You can create logger in another file using this and add the import  in main module. This will create a hierarchy 
```
import logging  
logger = logging.getLogger(__name__)  
logger.propagate = False # if don't want to create hierarchy  
logger.debug('This is a debug message')  
logger.info('This is an info message')  
logger.warning('This is a warning message')  
logger.error('This is an error message')  
logger.critical('This is a critical message')
```

- Creating Handlers: This code is not working but this is how you define an handler.
```
import logging  
logger = logging.getLogger(__name__)  
  
# create handler  
stream_h = logging.StreamHandler()  
file_h = logging.FileHandler('file.log')  
  
# level and the format  
stream_h.setLevel(logging.WARNING)  
file_h.setLevel(logging.ERROR)  
  
formatter = logging.Formatter('%(names -%(levelname)s - %(message)s')  
stream_h.setFormatter(formatter)  
file_h.setFormatter(formatter)  
  
logger.addHandler(stream_h)  
logger.addHandler(file_h)  
  
logger.warning('This is a warning')  
logger.error('This is an error')

```

- Tracing back issues:
  - If you know exceptions type:
```
try:  
    a = [1, 2, 3]  
    val = a[4]  
except IndexError as e:  
    logging.error(e, exc_info=True)
    
```


- If you don't know th exception type:
```
   import traceback
   
   try:  
    a = [1, 2, 3]  
    val = a[4]  
except :  
    logging.error("The error msg is %s", traceback.format_exc())

```

- Logging messages to files :
     -  Two ways:
          - #### Rotating Handler : 
```
logger = logging.getLogger(__name__)  
logger.setLevel(logging.INFO)  
  
# roll over 2KB, and keep backup logs app.log1, app.log2 etc.  
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
``` 

  
#### timed rotating handler  
```
timedHandler = TimedRotatingFileHandler('timed_app.log', when='s', interval=5, backupCount=5)  
logger.addHandler(timedHandler)  
  
for i in range(6):  
    logger.info("Hello World!")
    
```


- For a microservice architecture checkout python-json-logger on github

# JSON

- Converting an python object to json is serialization and the reverse process is de serialization.

- The python objects get converted to json in the following ways:
dictionary - object
list, tuple -array
float,long, int - number
True - true
False -false
str - string
null -none

Convert a dictionary to json  as a string: 
```
import json  
  
mydict = {"name": "Mary", "age": 28, "city": "Boston", "hasChildren": False}  
  
personJson = json.dumps(mydict, indent=4, sort_keys=True)  
print(personJson)

```

Convert a dictionary to json  as a file: 

```
 import json  
  
with open('person.json', 'w') as file:  
    json.dump(mydict, file, indent=4)
    
```

Convert a python object to json as a string:
```
# Convert a json object to python as string  
import json  

person = json.loads(personJson)  
print(person)

```

Convert a json object to python in a file  :
```
import json  

with open('person.json','r') as file:  
    person = json.load(file)  
    print(person)
    
```

Encode a custom python object using a self defined encode method:

```
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

```

Encode a custom python object using JSONencoder:
```
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

```

Decoding a custom object by defining a custom decoder :
```
# Decoding  
def decode_user(dct):  
    if User.__name__ in dct:  
        return User(name=dct['name'], age=dct['age'])  
    return dct  
  
  
user = json.loads(userJSON2, object_hook=decode_user)  
print(type(user))  
print(user.name)  
print(user)

```

# Random Numbers
- Random numbers can be generated using random , secrets module. They  generate pseudo random numbers - that are random but can be reproduced
- ## Using random module:

```
import random  
  
# generate a random float number  
a = random.random()  
print(a)  
  
# generate a random float number in the range  
a = random.uniform(1, 10)  
print(a)  
  
# generate a random int number in the range including the upper bound  
a = random.randint(1, 10)  
print(a)  
  
# generate a random int number in the range excluding the upper bound  
a = random.randrange(1, 10)  
print(a)  
  
# standard deviation in statistics  
a = random.normalvariate(0, 1)  
print(a)  
  
# choose a random  element string  
mylist = list('ABCDEFGH')  
a = random.choice(mylist)  
print(a)  
  
# choose random unique elements string of 3 and do not pick the same element twice  
a = random.sample(mylist, 3)  
print(a)  
  
# choose random elements string of 3 and can  pick the same element twice  
a = random.choices(mylist, k=3)  
print(a)

# shuffles the list in place  
random.shuffle(mylist)  
print(mylist)

# reproduce the number using seed method  
random.seed(1)  
print(random.random())  
print(random.randint(1, 10))  
  
random.seed(2)  
print(random.random())  
print(random.randint(1, 10))  
  
random.seed(1)  
print(random.random())  # will reproduce the same no. as in seed 1
print(random.randint(1, 10))  
  
random.seed(2) 
print(random.random())   # will reproduce the same no. as in seed 2
print(random.randint(1, 10))

```
- As they can be reproduced you should not use these for security purposes

## Using secrets module:
- These numbers can not be reproduced and they can be considered secure. But they take more time.
```
# generates a random number excluding upper bound  
a = secrets.randbelow(10)  
print(a)  
  
# generates a random number excluding upper bound in the range from 0000 bits to - 1111 bits(exclusive)  
a = secrets.randbits(4)  
print(a)  
  
a = secrets.choice(mylist)  
print(a)

```

- ## Using numpy:
  - generates a random number of elements as array
  - Always prefer to use numpy random module than python one

```
import random, secrets, numpy as np

# creates a float array of 3  
a = np.random.rand(3)  
print(a)  
  
# creates a float array of 3 by 3 size  
a = np.random.rand(3, 3)  
print(a)  
  
# creates a int array of 3 by 4 size  
a = np.random.randint(0, 10, (3, 4))  
print(a)  
  
# shuffles numoy array along the axis and not the numbers in place  
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
print(arr)  
np.random.shuffle(arr)  
print(arr)  
  
# np seed method np.random.seed(1)  
print(np.random.rand(3, 3))  
np.random.seed(1)  
print(np.random.rand(3, 3))

```

# Decoraters
- A decorater is a function that takes another function as an argument and extends the beahviour of the function without explicitly modifying it. In other words, it allows you to add new functionality to an existing function.
- In python functions are first class citizens. They can be passed as an argument in a function, returned from a function etc.
- Types of decorators:
   - ## Function Decorator:


```
 def start_end_decorator(func):  
    def wrapper():  
        print('Start')  
        func()  
        print('End')  
  
    return wrapper  
  
  
@start_end_decorator 
def print_name():  
    print('Alex')  
  
  
print_name()

```

If the function has arguments then:

```
def start_end_decorator(func):  
    def wrapper(*args, **kwargs):  
        print('Start')  
        result = func(*args, **kwargs)  
        print('End')  
        return result  
  
    return wrapper  
  
  
@start_end_decorator  
def print_name():  
    print('Alex')  
  
  
print_name()  
  
  
@start_end_decorator  
def add4(x):  
    return x + 4  
  
  
result = add4(10)  
print(result)

```

- For python to get not confused with identity of the function and the template for function decorator should be:

```
import functools  
  
  
def start_end_decorator(func):  
    @functools.wraps(func)  
    def wrapper(*args, **kwargs):  
        print('Start')  #do something before func call
        result = func(*args, **kwargs)  
        print('End')  #do something after func call
        return result  
  
    return wrapper  
  

  
@start_end_decorator  
def add4(x):  
    return x + 4  
  
  
result = add4(10)  
print(result)  
print(help(add4))  
print(add4.__name__)

```

- If a decorator has arguments then:
```

  
def repeat(num_times):  
    def decorator_repeat(func):  
        @functools.wraps(func)  
        def wrapper(*args, **kwargs):  
            for _ in range(num_times):  
                res = func(*args, **kwargs)  
            return res  
  
        return wrapper  
  
    return decorator_repeat  
  
  
@repeat(num_times=3)  
def greet(name):  
    print(f'Hello {name}')  
  
  
greet('Alex')

```

- We can apply multiple decorators, the first decorator will be executed first and inside first decorator the next decorator is executed.
```
@start_end_decorator  
@repeat(num_times=4)  
def say_hello(name):  
    greeting = f'Hello hoooolaaalaaa {name}'  
    print(greeting)  
    return greeting  
  
  
say_hello('Alex')
#Output:
# Start
# Hello hoooolaaalaaa Alex
# Hello hoooolaaalaaa Alex
# Hello hoooolaaalaaa Alex
# Hello hoooolaaalaaa Alex
# End


```

## Class decorators:
- They are typically used when you want to keep track of the state
```
class CountCalls:  
    def __init__(self, func):  
        self.func = func  
        self.num_calls = 0  
  
    def __call__(self, *args, **kwargs):  
        self.num_calls += 1  
        print(f'This is executed {self.num_calls} times')  
        return self.func(*args, **kwargs)  
  
  
@CountCalls  
def say_hello():  
    print('Hello')  
  
  
say_hello()  
say_hello()

```

Typical use cases of decorators:
- to debug and get more info about a function
- a timer decorator to calculate time taken by a function
- Add info ror update the state
- Cache info

# Generators
 - are functions that prdouces an object over which we can iterate. These objects are produced lazily and one by one. They are memory efficient. Use yield in place of return sattement

```
def my_generator():  
    yield 1  
    yield 2  
    yield 3  
  
  
g = my_generator()  
for i in g:  
    print(i)  
  
value = next(g)  
print(value)  
  
value = next(g)  
print(value)  
  
value = next(g)  
print(value)

```

with next() method the control goes to my_generator and then it pauses after first yield statement and  will produce a stop iterator error if does not reach a yield statement

```
import sys
def countdown(num):  
    print('Starting')  
    while num > 0:  
        yield num  
        num -= 1  
  
  
cd = countdown(4)  
value = next(cd)  
print(value)  
  
print(next(cd))  
  
  
def firstn(n):  
    nums = []  
    num = 0  
    while num < n:  
        nums.append(num)  
        num += 1  
    return nums  
  
  
def first_n_generator(n):  
    num = 0  
    while num < n:  
        yield num  
        num += 1  
  
  
print(sum(firstn(10)))  
print(sum(first_n_generator(0)))  
print(sys.getsizeof(sum(firstn(1000000))))  
print(sys.getsizeof(sum(first_n_generator(1000000))))

def fibonacci(limit):  
    a, b = 0, 1  
    while a < limit:  
        yield a  
        a, b = b, a + b  
  
  
fib = fibonacci(30)  
  
for i in fib:  
    print(i)

```


## Generator Expressions:
```
my_generator = (i for i in range(10) if i % 2 == 0)  
for i in my_generator:  
    print(i)
    
```

## Advantages:
- memory efficient
- do not need to wait until all the elements to be generated

# MultiProcessing vs Threading
- A process is a task in execution and a thread is a lighteweight program or entity that is part of a process. process occupies CPU space and thread does not

## Global Interpreter Lock
- Is a lock that allows python to run only one thread at a time
- Needed in C python because memory management is not thread safe
- Thus toa void using this GIL you can do the following:
   - Use Multiprocessing
   - Use different versions of python like IronPython
   - Use python as a wrapper for third party implementation eg. numpy etc.

```

from multiprocessing import Process  
import os  
import time  
  
  
def square_numbers():  
    for i in range(100):  
        i * i  
        time.sleep(0.1)  
  
  
processes = []  
num_processes = os.cpu_count()  
 
if __name__ == '__main__':  
    # create processes  
    for i in range(num_processes):  
        p = Process(target=square_numbers)  
        processes.append(p)  
  
    # start  
    for p in processes:  
        p.start()  
  
    # join processes  
    for p in processes:  
        p.join()
  
print('end main')  
  

```

Process do not share same memory space. Thus they can share values and arrays like this:
```
from multiprocessing import Process, Value, Array, Lock

def add_100(number, lock):  
    for i in range(100):  
        time.sleep(0.01)  
        with lock:  
            number.value += 1  
  
  
if __name__ == '__main__':  
 
    shared_number = Value('i', 0)  # i represent int  
    lock = Lock()  
    print('Number at the beginning is', shared_number.value)  
  
    p1 = Process(target=add_100, args=(shared_number, lock))  
    p2 = Process(target=add_100, args=(shared_number, lock))  
  
    p1.start()  
    p2.start()  
  
    p1.join()  
    p2.join()  
  
    print('Number at the end is', shared_number.value)  
  
print('end main')
```

Sharing Arrays:
```
from multiprocessing import Process, Value, Array, Lock
  
def add(numbers, lock):  
    for i in range(100):  
        time.sleep(0.01)  
        for i in range(len(numbers)):  
            with lock:  
                numbers[i] += 1  
  
  
if __name__ == '__main__':  
    
    shared_array = Array('d', [0.0, 100.0, 200.0])  # i represent double  
    lock = Lock()  
   
    print('Array at the beginning is', shared_array[:])  
  
    p1 = Process(target=add, args=(shared_array, lock))  
    p2 = Process(target=add, args=(shared_array, lock))  
  
    p1.start()  
    p2.start()  
  
    p1.join()  
    p2.join()  
  
    print('Array at the end is', shared_array[:])  
  
print('end main')

```

Use a queue to share between multiple processes:
```
def make_negative(numbers, queue):  
    for i in numbers:  
        queue.put(-1 * i)  
  
  
def cube(number):  
    return number * number * number  
  
  
if __name__ == '__main__':  
  
    numbers = range(1, 6)  
    q = Queue()  
    p3 = Process(target=square, args=(numbers, q))  
    p4 = Process(target=make_negative, args=(numbers, q))  
  
    p3.start()  
    p4.start()  
  
    p3.join()  
    p4.join()  
  
    while not q.empty():  
        print(q.get())
        
```

A process pool is one that manages the processes for you splits the processes into managable chunks etc.

## Threading:
```
# create threads  

from threading import Thread  
def square_numbers():  
    for i in range(100):  
        i * i  
        time.sleep(0.1)  
        
num_threads = 10  
threads = [] 

for i in range(num_threads):  
    t = Thread(target=square_numbers)  
    threads.append(t)  
  
for t in threads:  
    t.start()  
  
for t in threads:  
    t.join() # we wait and block the main thread until the thread is complete
    
```

To share values or data between threads:
```
from threading import Thread, Lock  
  
database_value = 0

def increase(lock):  
    global database_value  
  
    with lock:  # you should use a lock, if you don't race condition ahppens
        local_copy = database_value  
  
        # processing  
        local_copy += 1  
        time.sleep(0.1)  
        database_value = local_copy  
  
  
if __name__ == "__main__":  
    lock = Lock()  
    print('start value', database_value)  
  
    thread1 = Thread(target=increase, args=(lock,))  
    thread2 = Thread(target=increase, args=(lock,))  
    thread1.start()  
    thread2.start()  
  
    thread1.join()  
    thread2.join()  
    print('end value', database_value)  
print('end main')

```

A queue is thread safe.

```
  import time  
from threading import Thread, Lock, current_thread  
from queue import Queue

# q.put(1)  
# q.put(2)  
# q.put(3)  
#  
# first = q.get()  
#  
# q.task_done() # after you are done with processing queue element you should call task done  
# print(first)  
#  
# q.join() # block the main thread and wait until all the elements of q are done  
  
num_threads = 10  
  
  
def worker(q, lock):  
    while True:  
        value = q.get()  
  
        # processing  
        with lock:  
            print(f' in {current_thread().name} got {value}')  
        q.task_done()  
  
  
q = Queue()  
lock = Lock()  
  
for i in range(num_threads):  
    thread = Thread(target=worker, args=(q, lock))  
    thread.daemon = True  
    thread.start()  
  
for i in range(1, 21):  
    q.put(i)  
  
q.join()  
print('end')

```

# The asterisk operator
```
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

```

# Shallow copy and deep copy
```
import copy  
  
# shallow copy -only one level deep and copies reference of child object only  
org = [0, 1, 2, 3, 4]  
cpy = copy.copy(org)  #shallow
cpy[0] = -10  
print(cpy)  
print(org)  
  
# for a list you can also do this  
cpy = org.copy()  
# cpy =org[:]  
# cpy = list(org)  
cpy[0] = 10  
print(cpy)  
print(org)  
  
org = [[1, 2, 3, 4], [5, 6, 7, 8]]  
cpy = copy.copy(org)  
cpy[0][0] = -10  
print(cpy)  #changes both lists
print(org)  
  
# deep copy  
org = [[1, 2, 3, 4], [5, 6, 7, 8]]  
cpy = copy.deepcopy(org)  
cpy[0][0] = -10  
print(cpy)  
print(org)  
  
  
class Person:  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
  
  
class Company:  
    def __init__(self, boss, employee):  
        self.boss = boss  
        self.employee = employee  
  
  
p1 = Person('A', 24)  
p3 = Person('Joe', 79)  
p2 = copy.copy(p1)  
p2.age = 60  
print(p1.age)  
print(p2.age)  
  
company = Company(p1, p2)  
company_cpy = copy.deepcopy(company)  
company_cpy.boss.age = 90  
print(company_cpy.boss.age)  
print(company.boss.age)
```

# Context Managers
They allows us to manage resources and release resources. Commonly used for resource management

For example:
```
with open('notest.txt','w') as file:  
    file.write('some todo...')
```
this will allow to close the file evene if there is an exception and is recommended way to open a file

```
from threading import Lock

# without context manager
lock = Lock()  
lock.acquire()  
# do something  
lock.release()  
  
# with context manager  
with lock:  
    #....
```

## Implement a custom context manager using a class:
```
class ManagedFile:  
    def __init__(self, filename):  
        self.filename = filename  
  
    def __enter__(self):  
        print('Enter')  
        self.file = open(self.filename, 'w')  
        return self.file  
  
    def __exit__(self, exc_type, exc_val, exc_tb):  
        if self.file:  
            self.file.close()  
        if exc_type is not None:  
            print('exception')  
        #  print('exc:',exc_type,exc_val)  
        print('exit')  
        return True  
  
  
with ManagedFile('notes.text') as file:  
    print("Do some stuff todo...")  
    file.write("Some todo...")  
    file.somemethod()  
print('continuing....')

```

## Implement a custom context manager using a function:
```
from contextlib import contextmanager

@contextmanager  
def open_managed_file(filename):  
    f = open(filename,'w')  
    try:  
        yield f # all the code of enter function  
    finally: # all the code of exit fucntion  
        f.close()  
  
with open_managed_file('notes.txt') as f:  
    f.write('some toodoo')
    
```
