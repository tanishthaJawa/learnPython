# When to ue clqss methods and when to use static methods

class Item:
    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship with the class
        but not something that is unique per instance.
        '''

    @classmethod
    def instaniate_from_something(cls):
        '''
        This should so something that has a relationship with the class,
        but usually those that are used to manipulate different structures of data to instaniate objects, like we have done with CSV

        One difference from static and class method is that static method does not receive any reference but class method does

        Both of them can be called from an instance level but you rarely do that
        '''