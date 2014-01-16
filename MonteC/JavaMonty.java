/**
 * The JavaMonty class implements an application that
 * calculates Pi using Monte Carlo.
 */
 import java.lang.Math;
 import java.lang.Integer;
 
class JavaMonty {

	public double determinePi(int darts){
		int hitSum = 0;
		
		double x;
		double y;
		
		for (int i=0; i<darts;i++){
			x = Math.random();
			y = Math.random();
			
			if (Math.sqrt((x*x)+(y*y))<=1){
				hitSum++;
			}
			
		}
		
		// System.out.printf("%d : %d\n",hitSum,darts);
		double pic = 4.0*hitSum/darts;
		double error = Math.abs(100*(pic-3.1415926535897932)/(3.1415926535897932));
		return error;
	}
		
	public static void main(String[] args) {
		JavaMonty myJM = new JavaMonty();
		double error = myJM.determinePi(Integer.parseInt(args[0]));
		System.out.printf("%g\n",error);
    
	}
   
}

 