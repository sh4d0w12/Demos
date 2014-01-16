import threading
import time
from random import *
from numpy import *
'''
Caluclate Pi using a multiprocessor pool
'''
import sys
from time import sleep
import multiprocessing
import signal

def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    
def run_worker(darts):
    # print "Starting "
    
    dartCount=0
    hitsum=0
    for i in range(darts):
        x=random.random(1)
        y=random.random(1)
        
        if sqrt(x*x+y*y)<=1:
            hitsum+=1;
        
        dartCount+=1
        
    # print "Exiting ",
    return (hitsum,dartCount)
    
    
    
class collector (threading.Thread):
    
    def __init__(self, numberOfThreads, darts):
        threading.Thread.__init__(self)
        self.numberOfThreads = numberOfThreads
        self.darts = darts
        self.keepRunning = True
        self.result_list = []
        
    def run(self):
        self.pool = multiprocessing.Pool(self.numberOfThreads, init_worker)
        # print self.darts
        # print self.numberOfThreads
        result = self.pool.map_async(run_worker, [self.darts]*self.numberOfThreads)    
        self.pool.close()
        
        while(self.keepRunning):
            if result.ready():
                self.result_list = result.get()
                # print self.result_list
                break
            time.sleep(0.2)
        
    def cleanUp(self):
        self.pool.terminate()
    
    def getResult(self):
        error=None
        if any(self.result_list):
            total_hitsum = 0
            total_dartCount = 0 
            for re in self.result_list:
                total_hitsum+=re[0]
                total_dartCount+=re[1]
                # print re
                
            pic=4.0*total_hitsum/(total_dartCount)
            error=abs(100*(pic-3.1415926535897932)/(3.1415926535897932))
        return error
    


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
    