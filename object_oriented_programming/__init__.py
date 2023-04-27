from item import Item
from phone import Phone
from keyboard import Keyboard

# print(Item.pay_rate)
# print(item.pay_rate)  # access to class variable
# print(another_item.pay_rate)

# print(Item.__dict__)  # gets ALL THE ATTRIBUTES at the class level and converts it to dictioanry
# print(item.__dict__)  # ALL THE ATTRIBUTES at the instance level

# item.apply_discount()
# print(item.price)
#
# another_item.pay_rate = 0.7
# another_item.apply_discount()
# print(another_item.price)

# Item.instantiate_from_csv()
# print(Item.all)
#
# for instance in Item.all:
#     print(instance.name)
#
# print(Item.is_integer(7.0))
#
# phone1 = Phone(name="Phone", price=500, quantity=5, broken_phones=1)
# phone2 = Phone(name="Phone1", price=700, quantity=5, broken_phones=1)
# print(phone2.calculate_total_price())
#
# print(Item.all)
# print(Phone.all)

# getters and setters
item1 = Item("MyItem", 750)

# Getting an attribute
print(item1.name)

# setting an attribute
item1.name = "A"
print(item1.name)

item1.apply_increment(0.2)
print(item1.price)

# Abstraction
item1.send_email()
item2 = Keyboard("AA",100,0)
item2.apply_discount()
print(item2.price)