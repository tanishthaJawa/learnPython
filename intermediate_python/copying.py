import copy

# shallow copy -only one level deep and copies reference of child object only
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
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
print(cpy)
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
