// CplusMonte.cpp : Calculate value of Pi using Monte Carlo method
//
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>

#define getRandomFloat (float)rand() / (float)RAND_MAX;

using namespace std;

void determinePi(double &error, long darts){
	int hitSum = 0;

	double x;
	double y;

	for (int i = 0; i < darts; i++){
		x = getRandomFloat;
		y = getRandomFloat;
		//printf("x: %g   y: %g\n", x, y);
		
		if (sqrt((x*x) + (y*y)) <= 1){
			hitSum++;
		}

	}

	//printf("%d : %d\n", hitSum, darts);
	double pic = 4.0 * hitSum / darts;
	error = abs(100 * (pic - 3.1415926535897932) / (3.1415926535897932));
	
}

int main(int argc, char* argv[])
{
	//cout << argc << "\n";
	if (argc > 1){

		double error = NULL;
		long darts = strtol(argv[1], NULL, 10);
		//cout << darts<<"\n";
		determinePi(error, darts);
		cout << error << "\n";
		return 0;
	}
	else{
		return -1;
	}
		
}