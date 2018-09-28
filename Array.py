from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce


class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno= rollno
        self.lap   = self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand ='HP'
            self.ram   = 90
        def show(self):
            print(self.brand,self.ram)

s1 =student('hamid', 1)
s2 =student('Hafeez',2)

print(s1.show())
#lap1 = student.laptop()
