 import java.lang.Math;

class Problem implements Runnable{
	public int hitSum;
	public int darts;
	public int thrownDarts;
	
	public Problem(int darts){
		this.darts = darts;
		hitSum = 0;
		thrownDarts = 0;
	}
	
	public void run(){
		double x;
		double y;
		for (int i = 0; i<darts;i++){
			x = Math.random();
			y = Math.random();
			
			if (Math.sqrt((x*x)+(y*y))<=1){
				hitSum++;
			}
			thrownDarts++;
		}
		
		// System.out.printf("%d : %d\n",hitSum,thrownDarts);
	
	}

}