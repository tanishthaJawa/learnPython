from functools import reduce

add10 = lambda x: x + 10
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
print(b)
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

