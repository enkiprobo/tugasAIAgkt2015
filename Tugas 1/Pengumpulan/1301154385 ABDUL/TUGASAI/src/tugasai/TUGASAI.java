/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tugasai;

import static java.lang.Math.exp;
import java.util.Random;

/**
 *
 * @author abdulnursahid
 */
public class TUGASAI {
    /**
     *
     * @param args
     */
    public static void main(String[] args) {
        TUGASAI ai = new TUGASAI();
        int T = 500000;
        int dT =1;
        double fr = 1.5;
        double akurasi;
        double c1 = ai.acak(-10, 10);
        double c2 = ai.acak(-10, 10);
        double b1 = c1;
        double b2 = c2;
        double Eb = ai.fungsi(b1, b2);
        while (T > 0) {
            double n1 = ai.generateNew(c1);
            double n2 = ai.generateNew(c1);
            double En = ai.fungsi(n1, n2);
            double Ec = ai.fungsi(c1, c2);
            double De = En - Ec;
            if (De < 0) {
                c1 = n1;
                c2 = n2;                
                if (En < Eb){
                    b1 = c1;
                    b2 = c2;
                    Eb = Ec;
                } 
            }
            else {
                Random r = new Random();
                double s = r.nextDouble();
                if (s < (exp((-De)/T))){
                    c1 = n1;
                    c2 = n2;
                }
            }
           T = T - dT;
            
        }
            System.out.println("====");
            System.out.println("b1 = "+b1 +";"+" b2 = " +b2);
            System.out.println("Eb.. = "+Eb);
            akurasi = (1-((Eb- fr)/fr))*100;
            System.out.println("akurasi = "+akurasi);
    }
    public double fungsi(double a1, double a2){
        return (4-(2.1*(a1*a1))+((a1*a1*a1*a1)/3)*(a1*a1)+(a1*a2)+((-4+(4*(a2*a2))*(a2*a2))));
//        double n;
//        n = ((4 - ((2.1)*(a1*a1)) + ((a1*a1*a1*a1)/3))* (a1*a1))  + (a1*a2) + (((-4) + (4*(a2*a2))) * (a2*a2));  
//        return n;
    }
    
    public double acak (double mini, double maxi){
        Random a = new Random();
        double RandomJum = mini + (maxi- (mini)) * a.nextDouble();
        return RandomJum;
//    }
 //   public double probabilitas (double minstate, double newstate, double temp){
  //      return Math.pow(2.71828, (newstate-minstate)/temp);
  //  }
    }
    public double generateNew(double b){
        Random a = new Random();
        boolean c = a.nextBoolean();
        if (c) {
            b = b + 0.1;
        }
        else{
            b = b - 0.1;
        }
        return b;
        
    }
    
    
 //   public double random(){
 //       double a = 0;
 //       int maxi = 10;
 //       int mini = -10;
 //       
 //       Random b = new Random ();
//        int range = maxi-mini+1 ;
//        double random = b.nextInt(range)+mini;
//        if (random >= 0){
 //           a = random + b.nextDouble();
 //       }
 //       else{
  //          a = random - b.nextDouble();
   //     }
    //    return a;
 //   }

}
