/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication10;

import static java.lang.Math.random;
import java.util.Random;

/**
 *
 * @author toniebe
 */
public class JavaApplication10 {
    
 
 static double fungsi(double x1, double x2){
     return (4-(2.1*Math.pow(x1, 2))+((Math.pow(x1, 4))/3))*Math.pow(x1, 2)+(x1*x2)+(-4+(4*Math.pow(x2, 2)))*Math.pow(x2, 2);
 }
 
 static double prob(double minstate,double newstate,double temperatur){
    return Math.pow(2.71828183, minstate-newstate/temperatur);
 }
    
    
 static double random1 (double min, double max){
     
     double range = (max-min);
     return (Math.random()*range)+min;
 } 
    public static void main(String[] args) {
        
        
        double t = 9999;
        double ta = 0.9999;
        double x1 = random1(-10,10);
        double x2 = random1(-10,10);
        fungsi(x1,x2);
        double bof =  fungsi(x1,x2);
        
        while (t > ta){
            
            x1 = random1(-10,10);
            x2 = random1(-10,10);
            double ns = fungsi(x1,x2);
            
           if (bof > ns){
               bof = ns;
           }else{
               if (prob(bof, ns, t) > random1(0,1)){
                   bof = ns;
               }
            }
           
           t = t*ta;
          }
        System.out.println("x1: " +x1);
        System.out.println("x2: " +x2);
        System.out.println("hasil: "+bof);
        }
}
