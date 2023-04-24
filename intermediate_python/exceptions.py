# Errors and exceptions
# a = 5 + 's'  # TyeError
# import somemodule #import error
# a = 5
# b = c #NameError
# f = open('somefile.txt') #file not found error
# a = [1, 2, 3]
# a.remove(4) #ValueError
# a[4] #IndeError
# my_dict = {'name': 'Max'}
# age = my_dict['age'] #KeyError

# Exceptions
# x = -5
# assert (x >= 0, 'x is not positive')
# if x < 0:
#     raise Exception('x should be positive')

try:
    a = 5 / 1
    b = a + 10

except ZeroDivisionError as err:
    print(err)
except TypeError as err:
    print(err)
else:
    print('everything is fine')
finally:
    print("cleaning up")


class ValueTooHighError(Exception):
    pass


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
