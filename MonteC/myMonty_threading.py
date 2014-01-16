'''
Caluclate Pi using a threads
'''
import threading
import time
from random import *
from numpy import *
import sys
from time import sleep

class collector (threading.Thread):
    
    def __init__(self, numberOfThreads, darts):
        threading.Thread.__init__(self)
        self.numberOfThreads = numberOfThreads
        self.darts = darts
        self.keepRunning = True
        
    def run(self):
        self.threadList = []
        for i in range(self.numberOfThreads):
            self.threadList.append(problem(self.darts))
            self.threadList[-1].start()
            
        while(self.keepRunning):
            for th in self.threadList:
                if th.is_alive():
                    break;
                    
                self.keepRunning=False
            
        # for th in self.threadList:
            # print th.hitsum
    
    def cleanUp(self):
        for th in self.threadList:
            th.keepRunning=False
            
    
    def getResult(self):
        total_hitsum=0
        total_dartCount=0
        for th in self.threadList:
            total_hitsum+=th.hitsum
            total_dartCount+=th.dartCount
            
            # print th.hitsum
            # print th.dartCount
        
        pic=4.0*total_hitsum/(total_dartCount)
        error=abs(100*(pic-3.1415926535897932)/(3.1415926535897932))
        return error
    
class problem (threading.Thread):
    index=0
    
    def __init__(self, darts):
        threading.Thread.__init__(self)
        self.darts = darts
        problem.index+=1
        self.keepRunning=True
        self.hitsum=0
        
    def run(self):
        # print "Starting ",
        # print self.index
        self.dartCount=0;
        for i in range(self.darts):
            x=random.random(1)
            y=random.random(1)
            
            if sqrt(x*x+y*y)<=1:
                self.hitsum+=1;
            
            self.dartCount+=1
            
            if not self.keepRunning:
                break
            
        # self.pic=4.0*hitsum/self.darts
        
        # print "Exiting ",
        # print self.index


if __name__ == '__main__':
    if len(sys.argv)>2:
        # print determinePi(int(sys.argv[1]));
        # Create new threads
        thread1 = collector(int(sys.argv[1]),int(sys.argv[2]))
        thread1.start()
        while thread1.is_alive():
            try:
                sleep(0.5)
            except KeyboardInterrupt:
                thread1.keepRunning=False
        
        thread1.cleanUp()
        print thread1.getResult()
        