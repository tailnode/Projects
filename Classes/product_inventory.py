#!/usr/bin/env python3

class Product():
    def __init__(self, p, i, q):
        self.price = p
        self.id = i
        self.quantity = q

    def print_info(self):
        print('product id: %d, price: %d, quantity: %d' % (self.price, self.id, self.quantity))

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, *products):
        for i in products:
            self.products.append(i)

    def print_products(self):
        for i in self.products:
            i.print_info()

def test():
    p1 = Product(100, 102, 10)
    p2 = Product(10, 112, 100)
    p3 = Product(120, 122, 1)
    p4 = Product(140, 132, 0)

    inventory = Inventory()
    inventory.add_product(p1, p2, p3, p4)
    inventory.print_products()

test()
