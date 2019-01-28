import less5_function
import less5_function as l5f

from less5_function import are_square
from less5_function import square as sqr
print(dir(l5f))
print(dir(sqr))
print(dir())

import sys
import os

def print_path():
    for p in sys.path:
        print("'" +p+"'")

print_path()
sys.path.insert(0, os.getcwd() + '\\modules')
print_path()

import modules