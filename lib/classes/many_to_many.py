import math
class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("coffee name must be a str")
        if len(name) < 2:
            raise ValueError("coffee name must be >= 3 chars")
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in Order.all if order.coffee == self]))
    
    def num_orders(self):
        count = 0
        for order in Order.all:
            if order.coffee == self:
                count += 1
        return count
    
    def average_price(self):
        total = 0
        for order in Order.all:
            total += order.price
        result = total / len(Order.all)
        # return round(result)
        return (math.floor(result * 10) / 10)
    
class Customer:
    all = []
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("customer name must be a str")
        if len(name) < 1 or len(name) > 15:
            raise ValueError("customer name must be 1-15 chars")
        self._name = name
        Customer.all_customers(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("customer name must be a str")
        self._name = new_name

    @classmethod
    def all_customers(cls, new_customer):
        cls.all.append(new_customer)
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in Order.all if order.customer == self]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        highest = float(0.0)
        high_Customer = ""
        for order in Order.all:
            if order.coffee == coffee:
                if order.price > highest:
                    highest = order.price
                    high_Customer = order.customer
        if highest == 0:
            return None
        else:
            return high_Customer
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("customer must be from class")
        self._customer = customer
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be from class")
        self._coffee = coffee
        if not isinstance(price, float):
            if isinstance(price, int):
                price = float(price)
            else:
                raise ValueError("price must be a float")
        if price <= 1.0 or price >= 10.0:
            raise ValueError("price must be a float")
        self._price = price
        Order.all_orders(self)

    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @property
    def price(self):
        return self._price

    @classmethod
    def all_orders(cls, new_order):
        cls.all.append(new_order)