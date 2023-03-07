import sys
import requests

from random import randint

from projects.calculator.calculator import Calculator

my_calculator = Calculator()

def hello():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    return num1 + num2

if __name__ == '__main__':
    print (hello())
    print (sys.version)
    print (requests.__version__)