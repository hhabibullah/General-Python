from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce

import Calc
print(__name__)

result = Calc.add(5,4)
print(result)
print('********************')
result = Calc.sub(9,5)
print(result)
print('********************')

result = Calc.mult(5,4)
print(result)
print('******************')

result,re = Calc.div(20,4)
print(result,re)
print('******************')

