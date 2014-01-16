// CplusMonteThreaded.cpp : Calculate value of Pi using Monte Carlo method
//


//TODO: Create own structure to hold data for thread


#include <iostream>
#include <cmath>
#include <cstdio>
#include <windows.h>
#include <process.h>
#include <time.h>       /* time */
#include <stdlib.h>

//#define DEBUG
#define getRandomDouble (double)rand() / (double)RAND_MAX;

typedef unsigned long long uLong;

using namespace std;


struct WorkerStruct{
	uLong darts;
	uLong hitSum;
};

struct ProblemStruct{
	uLong darts;
	int numberOfWorkers;
	uLong result;
	WorkerStruct * arrayOfWorkers; // Array of worker structs
};




unsigned __stdcall secondFunc(void * pArguments){
	// Run independant simulation to determine number of hits
	
	WorkerStruct * threadArgs = (WorkerStruct *)pArguments;

	//printf("Thread ID: %d.\n", _threadid);
	srand(_threadid);  //Seed based on thread id
		
	threadArgs->hitSum = 0; // Reset the hitcount to 0
	
	double x;
	double y;

	for (int i = 0; i < threadArgs->darts; i++){
		x = getRandomDouble;
		y = getRandomDouble;
		#ifdef DEBUG
			printf("x: %g   y: %g\n", x, y);
		#endif // DEBUG
			
		if (sqrt((x*x) + (y*y)) <= 1){
			threadArgs->hitSum++;
		}

	}
	
	//printf("Hits %u :", threadArgs->hitSum);
	//printf("Darts %u\n", threadArgs->darts);
	return 0;
}


unsigned __stdcall threadFunc(void * pArguments){
	// Collector thread that spawns the worker threads
	
	ProblemStruct * myProblem = (ProblemStruct *)pArguments;
	myProblem->arrayOfWorkers = new WorkerStruct[myProblem->numberOfWorkers];

	HANDLE * threadList = new HANDLE[myProblem->numberOfWorkers];
	boolean allRunning = true;
	
	//cout << "Initialiszing\n";
	for (int i = 0; i < myProblem->numberOfWorkers; i++){
		myProblem->arrayOfWorkers[i].darts = myProblem->darts;
		
		threadList[i] = (HANDLE)_beginthreadex(NULL, 0, &secondFunc, (void *)(&myProblem->arrayOfWorkers[i]), 0, NULL);
	}

	//cout << "Running\n";
	while (allRunning){//While all the threads are acive wait
		allRunning = false;
		for (int i = 0; i < myProblem->numberOfWorkers; i++){
			if (WaitForSingleObject(threadList[i], 0) != WAIT_OBJECT_0){
				allRunning = true;
				break;
			}

		}
	}

	//cout << "Finishing\n";
	uLong totalHitSum = 0;
	uLong totalDarts = 0;
	
	for (int i = 0; i < myProblem->numberOfWorkers; i++){
		// Sum all the hits and darts
		//cout << myProblem->arrayOfWorkers[i].hitSum << "\n";
		totalHitSum += myProblem->arrayOfWorkers[i].hitSum;
		totalDarts += myProblem->arrayOfWorkers[i].darts;
		CloseHandle(threadList[i]);
		
	}
	
	//Copute estimated pi value
	double pic = 4.0 * (double)totalHitSum / (double)totalDarts;
	
	//printf("PIC %f\n", pic);
	double error = abs(100 * (pic - 3.1415926535897932) / (3.1415926535897932));
	printf("%g\n", error);

	//Free up memory
	delete []myProblem->arrayOfWorkers;
	delete []threadList;
	
	return 0;

}

int main(int argc, char* argv[])
{
		
	if (argc > 2){
		
		HANDLE hThread;
		unsigned threadID;

		double error = NULL;
		int numberOfThreads = (uLong)strtol(argv[1], NULL, 10);
		uLong darts = strtol(argv[2], NULL, 10);;

		ProblemStruct * myProblem = new ProblemStruct;
		myProblem->darts = darts;
		myProblem->numberOfWorkers = numberOfThreads;
		
		hThread = (HANDLE)_beginthreadex(NULL, 0, &threadFunc, (void *)myProblem, 0, &threadID);
		WaitForSingleObject(hThread, INFINITE);
		CloseHandle(hThread);
		
		delete myProblem;
						
		return 0;
	}
	else{
		return -1;
	}
	
	
}