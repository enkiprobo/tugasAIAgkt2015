/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package simulated.annealing;
import static java.lang.Math.exp;
import java.util.Random;
/**
 *
 * @author Ressa f
 */
public class SimulatedAnnealing {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Random random = new Random();
        double newState, minState;
        double newX1 = 0;
        double newX2 = 0; 
        double bestSoFar = 10;
        double T = 5000;
        newState = getFungsi(newX1, newX2);
        minState = newState;
        while (T >= 0.01){
            newX1 = random.nextInt(20) + (-10) - random.nextDouble();
            newX2 = random.nextInt(20) + (-10) - random.nextDouble();
            newState = getFungsi(newX1, newX2);
            if (newState < minState){
                minState = newState;
                bestSoFar = newState;
            } else {
                double deltaE = Math.pow(exp(1),-(newState - minState)/T);
                double r = Math.random();
                if (deltaE > r){
                    minState = newState;
                }
            }
            T = 0.997 * T;
        }
        System.out.println("F(x1,x2) = " + bestSoFar);
        double Fa = bestSoFar;
        double Fr = 0.8;
        double akurasiModel = (1 - ((Fa - Fr)/Fr)) * 100;
        System.out.println("Akurasi Model = " + akurasiModel);
    }
    
    public static double getFungsi(double x1, double x2) {
        double hasil, kurung;
        kurung = (4-2.1*Math.pow(x1, 2)+Math.pow(x1,4));
        hasil = (kurung * Math.pow(x1, 2)) + x1*x2 + (-4+4*Math.pow(x2, 2)*Math.pow(x2, 2));
        return hasil;
    }
}
