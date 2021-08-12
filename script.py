# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:11:10 2021

@author: ali1
"""
import requests

# print(sys.version)
# print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

r = requests.get("https://coreyms.com")
print(r.status_code)
