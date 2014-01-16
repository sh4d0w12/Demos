/**
 * The JavaMontyThread class implements an application that
 * calculates Pi using Monte Carlo. It uses threads in order to take
 * advantage of the multiple cores
 */

import java.lang.Integer;
import java.lang.Thread;
import java.lang.Exception;
 
class JavaMontyThreaded {
	
    public static void main(String[] args) {
		Collector myCollector = new Collector(Integer.parseInt(args[0]),Integer.parseInt(args[1]));
		Thread collectorThread = new Thread(myCollector);
		collectorThread.start();
		while (collectorThread.isAlive()){
            try{
				Thread.sleep(500);
			}catch (Exception Err){
				System.out.println("Error");
			}
        }    
		
		System.out.printf("%g\n",myCollector.error);
    }
}