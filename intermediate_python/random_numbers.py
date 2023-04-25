import random, secrets, numpy as np

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
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

# generates a random number excluding upper bound
a = secrets.randbelow(10)
print(a)

# generates a random number excluding upper bound in the range from 0000 bits to -1111 bits(exclusive)
a = secrets.randbits(4)
print(a)

a = secrets.choice(mylist)
print(a)

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

# np seed method
np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))
