/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sa;

import java.util.Random;

/**
 *
 * @author Geb
 */
public class SA {
    private static double StatAkhir;
    private static double StatAwal;
    private static double loopan = 5000;
    private static double temp1;
    private static double temp2;
    private static double alpha = 0.89597;
    private static double live;
    private static double hasil;
    private static double probs;
    private static double exp = 2.71828183;
    
    
    public static double Ran() {
        Random ran = new Random ();
        double dum = ran.nextInt(20)+(-10)-ran.nextDouble();
        return dum;
    }
    
    
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        while (loopan > 0.522) {
            for (int i = 0; i < 100; i++) {
                temp1 = Ran();
                temp2 = Ran();
                StatAwal = (4-2.1*temp1*temp1 + (Math.pow(temp1,4)/3))*temp1*temp1+temp1*temp2+(-4+4*temp2*temp2)*temp2*temp2;
                if (hasil > StatAwal) {
                    hasil = StatAwal;
                } 
                else if (StatAwal > hasil) {
                    double deltaE = -(StatAwal-hasil)/loopan;
                    probs = Math.pow(exp,deltaE);
                    if (probs>Math.random()) {
                        hasil = StatAwal;
                    }
                }                
            }
            loopan = loopan * alpha;
            
            
            
        }
        System.out.println(temp1);
        System.out.println(temp2);
        System.out.println(hasil);
        
    
    }   
}
