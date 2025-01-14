from __future__ import print_function
import math,sys
from decimal import *

getcontext().rounding = ROUND_FLOOR     # This line will round the numbers down to  the closest integer

VPython=sys.version_info[0]==2          # This check if python's version is 2.x
if VPython:
    input=raw_input         # On python2 the function <i>Input</i> was <i>raw_input</i>


def getValueOfe(n:int):
    """
    Function that return formated number given the number of decimal digitis 

    Inputs: n -> Number of decimal digitis
    """
    return '%.*f' % (n, math.e) 


def main():
    print("In the shell below Enter the number of digits upto which the value of e should be calculated or enter quit to exit\nMaximun of 53 digits")
    while True:
        print(">>>", end="")
        entry=input()
        if entry=="quit":
            break
        if not entry.isdigit():
            print("Please insert a number")
        else:
            print(str(getValueOfe(int(entry))).rstrip('0'))

if __name__=="__main__":
    main()