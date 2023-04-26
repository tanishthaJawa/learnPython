import sys


def my_generator():
    yield 3
    yield 2
    yield 3


g = my_generator()
# print(sum(g))

print(sorted(g))
for i in g:
    print(i)


# value = next(g)
# print(value)
#
# # will produce a stop iterator error if does not reach a yield statemen
# value = next(g)
# print(value)
#
# value = next(g)
# print(value)

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

my_generator = (i for i in range(10) if i % 2 == 0)
for i in my_generator:
    print(i)
