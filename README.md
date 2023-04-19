# Python
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
from math import *
and then use floor(3.8)

to get first character from a string avriable we use [] to acces it.
For example: name ="hila" , we can do name[0] to access h

## **List:**
is a data structure that allows us yo store ordered, mutable,duplicate and same/different  types of values. 

The syntax is :
friends = ["karen", True,2]

Forward indexing starts from 0 and backward indexing starts from -1. 
You can also specify a range 
for ex: friends[1:3] - this will get all elemnets after index 1 excluding 3 index

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

# **Tuple:**
is an ordered data structure that allows us to store values which can not be changed. They are immutable. Generally used to store data that need not to be changed. Tuples are faster and more efficient than lists. To store the same amount of data a tuple would be a wiser choice if a data set is quite large.

Forward indexing starts from 0 and backward indexing starts from -1.

The syntax is:

- coordiantes =(8,10) 
- mytuple2 = "Max", 32  # the brackets are optional
- tuple(iterable_data_str): will create a tuple for you
- If you put a single element inside a tuple it will not recognise it as a tuple, inside. it will recognise it as a string or an int or whatever, and thus you need to do this for it to be recognised as a tuple: mytuple3 = (32,)  # put a comma at the end

### Common Functions:
- count(element) - counts the occurance of an elemnent in tuple.
- index(element) - finds the index of an element

You can easily convert a list to tuple and vice versa using list(tuple_name) and tuple(list_name) respectively.
to access it : coordinates[0] will give 8

### Examples
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
print(i1)  a
print(i2)  ['p', 'p', 'l'] : is a list containing leftover elements
print(i3) e

# **Dictionary:**
- is an unordered and mutable data structure that allows us to store data in the form of keys and values . 

- The syntax is: 
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

### Common Functions:
- pop(key_name) - removes a key value pair of given key name
- popitem() - rmeoves last inserted key value pair
- keys - returns a list of keys
- values - returns a list of values
- items - returns both key and value
- update - merges two dictionaries and update them
- get(keyname,default value) - gets a value for the keyname and allows you to specify a default value

The keys can only be of immutable types. If using a number as a key, ensure that you never access the dictionary using the index value then.  

For example: mydict5 = {3: 9, 4: 16}  
value = mydict5[3]  
print(value)

You can also use a tuple as a key but do not use a list as a key because they are of mutable types. For example:
mytuple = (8, 7)  
mydict6 = {mytuple: 15}  
print(mydict6)

### Examples:
del mydict["name"]  # default del method
print(mydict)  
  
mydict.pop('age')  
print(mydict)  
  
mydict.popitem()  # removes last item
print(mydict)

#### Iteration
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

You can make a comment using # and multiple lines comment using ''' three quotes

# Sets
- is an unordered and mutable data structure that allows us to store data but unlike lists and tuples do not allow duplicate elements.
- The syntax is :
myset ={1,2,3}
or 
myset2 = set(iterable)

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
- For example : a = frozenset([1, 2, 3, 4])
- adding, removing or any other operations will produce an error if done on frozenset.

# Strings
- is an ordered, immutable collection data type that is used for text representation. It is the msot commonly used datatype.
- Syntax:
- Can use a single quote or double quote,single quote is more common though
    my_string = 'Hello World'  
print(my_string)  
  
my_string2 = """Hello  # Triple string used for string to run on new line
World"""  
print(my_string2)
- Can access elements like this:
char = my_string[0]  
print(char)
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
 var = "Tom"  
 my_string = "the variavle is %s" % var  
 print(my_string)  
  
var = 3  
my_string = "the variavle is %d" % var  
print(my_string)  
  
var = 3.2211  
my_string = "the variavle is %.2f" % var  # here %.2f indicates that it is floating point and we want only two digits after decimal. You can use %f as well
print(my_string)
     - format, 
     - f strings 
 
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

- ###### f strings
var2 = 6  
my_string = f "the variable is {2*var} and {var2}"  # evaluates variable values in run time
print(my_string)


### Examples:
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


# Function syntax:
def function_name():
       print("say Hi")


function_name()

# if else syntax:
if is_male and is_tall:  
    print("You are a male and tall ")  
elif is_male and not is_tall:  
    print("short male")  
elif is_tall and not is_male:  
    print("tall female")  
else:  
    print("You are  short female ")

# Loops:
i = 1  
while i <= 10:  
    print(i)  
    i += 1  
print("loop ended")  
  
friends = ["Jim", "karen"]  
for letter in friends:  
    print(letter)

# Try syntax:
try:  
    value = 10 / 0  
    num = int(input("Enter a number"))  
    print(num)  
except ZeroDivisionError as err:  
    print(err)  
except ValueError:  
    print("Invalid Value")

# Reading/Writing/Appending Files: 
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
employee_file = open("employees.txt", "r")  
 print(employee_file.readline())  
 print(employee_file.readline())  
 print(employee_file.readlines()[1])  
  
for employee in employee_file.readlines():  
    print(employee)  
  
    employee_file.close()

# Modules
- These are essentially useful files containing useful functions that you would like to import in your code.
They are of three types:
- Built in : already available in python
- External modules : in lib folder of external libraries
- External third party modules : found in site - package
- The syntax is :
import  filename
  
print(filename.methodName())
- The pip is a package manager to install different modules

# Classes
class Student:  
  
    def __init__(self, name, major, gpa, is_on_probation):  
        self.name = name  
        self.major = major  
        self.gpa = gpa  
        self.is_on_probation = is_on_probation  
  
  
student1 = Student("nia", "science", 4.9, True)  
print(student1.name)

To import in another file we would write it as
from Student import Student 
meaning from student file import student datat type

# inheritance
Syntax:
from parent import parent
child_class(Parent class)


