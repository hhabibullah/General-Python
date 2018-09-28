from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce


class computer:

    def config(self):
        print('Hello world')
        print('I am Hamid')

com1 = computer()
com2 = computer()

computer.config(com1)# one way of calling to a method in a class
computer.config(com2)
print('Second way of calling to a method in a class is following')

com1.config()  # second way of calling to a method in a class
com2.config()