# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 14:05:26 2021

@author: chomi
"""

import os 

path = 'images/'
zero = open("0.txt", "w+")
for filename in os.listdir('images/0/'):
    zero.write(filename + '\n')
zero.close()

one = open("1.txt", "w+")
for filename in os.listdir('images/1/'):
    one.write(filename + '\n')
one.close()

two = open("2.txt", "w+")
for filename in os.listdir('images/2/'):
    two.write(filename + '\n')
two.close()

thr = open("3.txt", "w+")
for filename in os.listdir('images/3/'):
    thr.write(filename + '\n')
thr.close()

four = open("4.txt", "w+")
for filename in os.listdir('images/4/'):
    four.write(filename + '\n')
four.close()