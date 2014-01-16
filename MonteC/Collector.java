import java.lang.Thread;
import java.lang.Math;

class Collector implements Runnable{
	
	private int darts;
	private int numberOfThreads;
	private boolean keepRunning;
	public double error;
	
	public Collector(int numberOfThreads,int darts){
		this.darts = darts;
		this.numberOfThreads = numberOfThreads;
		this.keepRunning = true;
	}
	
	public void run(){
		Problem []myProblems = new Problem[numberOfThreads];
		Thread []problemThreads = new Thread[numberOfThreads];
		
		for(int i=0; i<numberOfThreads; i++){
			myProblems[i] = new Problem(this.darts);
            problemThreads[i] = new Thread(myProblems[i]);
			problemThreads[i].start();
		}
		
		boolean resultReady;
		
		waitingLoop:
		while (keepRunning){
			
			resultReady = true;
			for (Thread th: problemThreads ){
				if (th.isAlive()==true){
					resultReady = false;
					break;
				}		
			}	
			
			if (resultReady){
				break waitingLoop;
			}
		}
				
		long totalHitSum = 0;
		long totalDarts = numberOfThreads*darts;
		
		for (Problem pr: myProblems ){
			// System.out.printf("%d %d\n",pr.hitSum, pr.thrownDarts);
			totalHitSum += pr.hitSum;
		}
		
		double pic = 4.0*totalHitSum/totalDarts;
		// System.out.printf("%g  %d: %d\n",pic,totalHitSum,totalDarts);
		error = Math.abs(100*(pic-3.1415926535897932)/(3.1415926535897932));
			
	}

}