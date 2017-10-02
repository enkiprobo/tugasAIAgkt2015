package tubesAI;

import java.util.Random;


public class tubesAI {
    
     public static double fungsi(double x1, double x2){
            return ((4-2.1*x1*x1+x1*x1*x1*x1/3)*x1*x1 +x1*x2+(-4+4*x2*x2)*x2*x2);
        }
     
     public static double  bebas(double min, double max){
        Random s = new Random();
        double angkarandom = s.nextDouble();
        return angkarandom;
    }
     
    public static void main(String[] args) {
        double x1;
        double x2; 
        double min = -10 ;
        double max = 10;
        double t = 0.001 ;
        double takhir = 0.8;
        double a = 0.0000000007;
        double e = 2.71828183;
        double probabilitas;
        x1= bebas(min,max);
        x2= bebas(min,max);
        bebas(min,max);
        double newstate = fungsi(x1,x2);
        double minstate = fungsi(x1,x2);
        double nilaisementara = fungsi(x1,x2);
        while(t > takhir){
                x1 = bebas( min,max);
                x2 = bebas( min,max);
                probabilitas = Math.pow(e,(minstate-newstate)/t);
                if (nilaisementara > newstate){
                    nilaisementara = newstate;
                }
                else {
                   if  (probabilitas > bebas(max,min)){
                     nilaisementara = newstate;  
                   }  
                }
            t = a*t;
            
        }
        System.out.print("x1 = ");
        System.out.println(x1);
        System.out.print("x2 = ");
        System.out.println(x2);
        System.out.print("hasil = ");
        System.out.println(nilaisementara);
       
    }
    
}
