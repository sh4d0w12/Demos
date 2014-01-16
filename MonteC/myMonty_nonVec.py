'''
Non-numpy based solution for calculating Pi (Very slow)
'''
from random import *
from numpy import *
import sys
import timeit

def determinePi(darts):
    
    hitsum=0
    for i in range(darts):
        x=random.random(1)
        y=random.random(1)
        
        if sqrt(x*x+y*y)<=1:
            hitsum+=1;
     
    
    pic=4.0*hitsum/darts
    
    error=abs(100*(pic-3.1415926535897932)/(3.1415926535897932))
    return error

if __name__ == '__main__':
    if len(sys.argv)>1:
        print determinePi(int(sys.argv[1]));
        
        