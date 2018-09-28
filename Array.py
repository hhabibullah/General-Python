from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce


class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Hello what is the name of your cpu and how much ram',self.cpu,self.ram)

com1 = computer('E5',56) #Learning how to use constructor
com2 = computer('r5',24)

com1.config()  # second way of calling to a method in a class
com2.config()