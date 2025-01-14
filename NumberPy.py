from __future__ import print_function
import math,sys
from decimal import *

getcontext().rounding = ROUND_FLOOR     # This line will round the numbers down to  the closest integer
sys.setrecursionlimit(100000)           # Set the maximun amount for a recursive function

VPython=sys.version_info[0]==2          # This check if python's version is 2.x
if VPython:
    input=raw_input         # On python2 the function <i>Input</i> was <i>raw_input</i>

def factorial(n:int):
    """
    Recursiv function that return the factorial of a number 

    Inputs: n -> Number that will be factoraded 
    """
    if not n:
        return 1
    return n*factorial(n-1)             # for definition n!=n*(n-1)*(n-2)*...*1

def getIteratedValue(k:int):
    """
	Return the Iterations as given in the Chudnovsky Algorithm.
	k iterations gives k-1 decimal places.
    Since we need k decimal places make iterations equal to k+1
	
	Inputs:	k -> Number of Decimal Digits to get
	"""
    k=k+1
    getcontext().prec=k
    sum=0
    for k in range(k):
        dividend = factorial(6*k)*(13591409+545140134*k)
        divisor = factorial(3*k)*((factorial(k))**3)*((-262537412640768000)**k)
        sum += dividend/divisor     # https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    return Decimal(sum) 

def getValueOfPi(k:int):
    """
	Returns the calculated value of Pi using the iterated value of the loop
	and some division as given in the Chudnovsky Algorithm
	Input: k -> Number of Decimal Digits upto which the value of Pi should be calculated
	"""
    iterator=getIteratedValue(k)
    up=426880*math.sqrt(10005)
    pi=Decimal(up)/iterator			# https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    return pi

def main():
    print("In the shell below Enter the number of digits upto which the value of Pi should be calculated or enter quit to exit")

    while True:
        print(">>>", end="")
        entry=input()
        if entry=="quit":
            break
        if not entry.isdigit():
            print("Please insert a number")
        else:
            print(getValueOfPi(int(entry)))

if __name__=="__main__":
    main()