myset = {1, 2, 3}
print(myset)

myset2 = {12, 3, 4}
print(myset2)

myset3 = set("Hello")
print(myset3)

myset4 = set()
myset4.add(1)
myset4.add(2)
myset4.add(3)
myset4.remove(2)
myset4.discard(3)
print(myset4)
myset4.add(2)
myset4.add(3)
print(myset4.pop())

for i in myset2:
    print(i)
if 4 in myset4:
    print("yes")
odds = {1, 3, 5, 7}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

diff = odds.difference(primes)
print(diff)

diff2 = evens.symmetric_difference(primes)
print(diff2)

odds.update(evens)
print(odds)

primes.intersection_update(evens)
print(primes)

odds.difference_update(evens)
print(odds)

evens.symmetric_difference_update(primes)
print(evens)

setA = {1, 2, 3, 4, 5, 6, 7, 8}
setB = {1, 2, 3}

print(setA.issuperset(setB))
print(setA.issubset(setB))
print(setA.isdisjoint(setB))

a = frozenset([1, 2, 3, 4])

