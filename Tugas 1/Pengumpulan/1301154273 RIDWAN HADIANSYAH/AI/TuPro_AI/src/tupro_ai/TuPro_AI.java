/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tupro_ai;
import java.util.Random;
import static java.lang.Math.random;

public class TuPro_AI {
    //private int temp;
    //private double newstateX1, newstateX2;

    
 /*   public TuPro_AI() {
    } */
    
    public static double random1(){
        double newstateX1 = (double) -10.0;
        double newstateX2 = (double) 10.0;
        Random random = new Random();
        double r = newstateX1 + random.nextDouble() * (newstateX2 - newstateX1)  ;
        return r;
    }
    
      public static double random2(){
        double newstateX1 = (double) 0.0;
        double newstateX2 = (double) 1.0;
        Random random = new Random();
        double r = newstateX1 + random.nextDouble() * (newstateX2 - newstateX1)  ;
        return r;
    }
    
     public static double rumus(double x1, double x2){
        double penampung = (4 - (2.1*(Math.pow(x1, 2)))+((Math.pow(x1, 4))/3))*(Math.pow(x1, 2)) + (x1*x2) + (-4+(4*(Math.pow(x2, 2))))*(Math.pow(x2, 2));
        return penampung;
     }
        
    /**
     *
     * @param args
     */
    public static void main(String[] args) {
        double Tawal = 10000;
        double Takhir = 1;
        double xAwal1,xAwal2,x,xAkhir1,xAkhir2,nilaiAwal,nilaiAkhir;
        xAwal1 = random1();
        xAwal2 = random1();
        nilaiAwal = rumus(xAwal1, xAwal2);
        xAkhir1 = 0; 
        xAkhir2 = 0;
        while(Tawal>Takhir){
            for(int j=100;j>0;j--){
            xAkhir1 = random1();
            xAkhir2 = random1();
            nilaiAkhir = rumus(xAkhir1, xAkhir2);
            x = random2();
            if(nilaiAwal>nilaiAkhir){
                nilaiAwal = nilaiAkhir;
            } else if(Math.pow(2.71828183,((nilaiAwal - nilaiAkhir)/Tawal)) > x) {
                nilaiAwal = nilaiAkhir;
            }
            
        }
       Tawal = Tawal *0.8; 
    }
        System.out.println("Nilai Awal 1 : " +xAwal1);
        System.out.println("Nilai Awal 2 : " +xAwal2);
        System.out.println("Nilai Akhir 1 : " +xAkhir1);
        System.out.println("Nilai Akhir 2 : " +xAkhir2);
        System.out.println("Nilai : "+nilaiAwal);
}
}
       
        //Math.pow(2.71828183,((nilaiMinAwal - minBaru)/tempawal)) > x3
        



