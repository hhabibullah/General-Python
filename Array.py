from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce


class Car:
    wheel = 4
    def __init__(self):
       self.mil = 10
       self.model = 'BMW'


c1 = Car()
c2 = Car()
c1.mil =8
Car.wheel = 3

print(c1.mil,c1.model,c1.wheel)
print(c2.mil,c2.model,c2.wheel)