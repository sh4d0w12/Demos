'''
Caluclate Pi using Numpy
'''

from random import *
from numpy import *
import sys
import timeit

def determinePi(darts):
    
    x=random.random(darts)
    y=random.random(darts)
    one=ones(darts)

    dist=sqrt(x*x+y*y)
    # print "dist ",dist
    hit=(less_equal(dist,one)==True)
    # print "hit ",hit
    hits=sort(hit)
    # print "hits ",hits
    # hitsnum=hits.searchsorted(True, side="right") - hits.searchsorted(True, side="left")
    hitsnum=sum(hits==True)
    # print "hitsnum ",hitsnum

    pic=4.0*hitsnum/darts
    # print "Pi calculated as ",pic
    error=abs(100*(pic-3.1415926535897932)/(3.1415926535897932))
    # print "Error is ", error, "%"
    return error

if __name__ == '__main__':
    if len(sys.argv)>1:
        print determinePi(int(sys.argv[1]));
        
        