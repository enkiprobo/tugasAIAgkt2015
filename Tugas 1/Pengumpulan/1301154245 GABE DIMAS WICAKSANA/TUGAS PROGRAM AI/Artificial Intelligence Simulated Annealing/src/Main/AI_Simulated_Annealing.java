//NAME    : GABE DIMAS WICAKSANA
//NIM     : 1301154245
//CLASS   : ARTIFICIAL INTELLIGENCE IF 39-07
//
//Artificial Intelligence Final Project for SEARCHING Topic

package Main;
import java.util.Random;

public class AI_Simulated_Annealing {

    public static void main(String[] args) {
        double loop = 1000;
        double x1,x2;
        double alpha = 0.99;
        double currentstate = 0;
        double BEST_SO_FAR = 10;
        double newstate,probability;
        double e = 2.71828183;
        double accuracy;

        while(loop >= 0.01) {
            x1 = randomX();
            x2 = randomX();
            newstate = function(x1,x2);
            
            if (newstate < currentstate) {
                currentstate = newstate;
                BEST_SO_FAR = newstate;
            } else if (newstate > currentstate) {
                probability = Math.pow(e,(currentstate - newstate)/loop);
                if (probability > Math.random()) {
                       currentstate = newstate;
                }
            }
            loop = loop * alpha; 
        }
        
        accuracy = (1 - ((BEST_SO_FAR - 1.5)/1.5)) * 100;
        
        System.out.print("Minimal answer : ");
        System.out.println(BEST_SO_FAR);
        System.out.print("Accuracy : ");
        System.out.print(accuracy);
        System.out.println(" %");
    }
    
    public static double function(double x1, double x2){
        double function = (4 - (2.1 * (x1*x1)) + ((x1*x1*x1*x1)/3)) * (x1*x1) + (x1*x2) + (-4 + (4 * (x2*x2))) * (x2*x2);
        return function;
    }
    
    public static double randomX() {
        Random randX = new Random();
        double numX = randX.nextInt(20) + (-10) - randX.nextDouble();
        return numX;
    } 
}