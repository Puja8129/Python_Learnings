#!/bin/python3

import math
import os
import random
import re
import sys

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year% 400 == 0:
                return True
            else:  
                return False
        else: 
            return True
    else:
        return False
    


            

if __name__ == '__main__':
    # n = int(input().strip())
    
    # if n%2==1:
    #     print("weird")

    n= input().strip()

    if n==" ":
        char ="a"
        print("Anish")
    if n==" ":
        char = "p"
        print("Puja")    
