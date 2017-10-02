/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tubes;

import java.util.Random;

/**
 *
 * @author Ivana A
 */
public class TUBES {
    static double x(double x1, double x2){ 
        return (4-2.1*x1*x1+x1*x1*x1*x1/3)*x1*x1+x1*x2+(-4+4*x2*x2)*x2*x2;
    }
    static double probabilitas(double minimumstate, double newstate, double temperature){
        return Math.pow(2.71828183, -1*(minimumstate-newstate)/ temperature);
    }
    static double ran(double nmin,double nmax){
        Random r = new Random();
        double randomValue = nmin + (nmax - (nmin)) * r.nextDouble();
        return randomValue;
                
    }
    public static void main(String[] args) {
        double temperature, i, alpha,x1,x2,minimumstate,newstate;
        temperature = 100000;
        alpha = 0.999;
        x1=ran(-10,10);
        x2=ran(-10,10);
        minimumstate=x(x1,x2);
        while (temperature>=0.01){
            x1 = ran(-10,10);
            x2 = ran(-10, 10);
            newstate =x(x1,x2);
           if(minimumstate>newstate){
               minimumstate=newstate;
           }
            temperature= alpha*temperature;  
        }
        System.out.println(minimumstate);
    }
}