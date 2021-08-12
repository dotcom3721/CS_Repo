# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:11:10 2021

@author: ali1
"""
import sys

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

print(greet('world'))
print(greet('Corey'))
