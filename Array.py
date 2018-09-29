from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce
from threading import *
from time import sleep

f = open('ABC','r')
f1= open('wer','w')
#f1.write('\nwhat about the other people and what about the other guys')
#print(f1.readline(),end = '#')
#print(f1.readline(),end = '#')

for data in f:
    f1.write(data)

