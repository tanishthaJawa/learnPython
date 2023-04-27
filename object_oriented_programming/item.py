import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # property decorator - read only attribute makes a field read only
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        # pay_Rate should only be accessed using object instead of class inside a method like this
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too Long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    # changes the way we represent objects inside our all list
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}',{self.__price},{self.quantity})"

    # methods defined on class
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    # static method
    @staticmethod
    def is_integer(num):
        # We will count out floats that are point 0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __connect(self, stmp_server):
        pass

    def __prepare_body(self):
        return f"Hello Someone." \
               f"We have {self.__name} {self.quantity} times" \
               f"Regards, Jim"

    def send_email(self):
        self.__connect("Hi")
        self.__prepare_body()
        self.__send()

    def __send(self):
        pass
        