/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tugasai;

/**
 *
 * @author GL552JX
 */
import java.text.DecimalFormat;
import java.util.Random;

public class TugasAI {

    /**
     * @param args the command line arguments
     */
public static double rumus(){
        double x1=Math.random()* 10+(-10);
        double x2=Math.random()* 10+(-10);
        return ((4-(2.1*(x1*x1))+((x1*x1*x1*x1)/3))*(x1*x1))+(x1*x2)+((-4+(4*(x2*x2)))*(x2*x2));
    }    
    
    public static void main(String[] args) {
        // TODO code application logic here
        
        double awal=0;
        double akhir=0;
        double rate = 0.9999;
        double tmp = 3;
        awal=rumus();
        while (tmp>1) {
            akhir=rumus();
            if(akhir<awal){
                awal=akhir;    
            }else
                
            {
                if (Math.exp(-1*((akhir-awal)/tmp))> Math.random()*1+0){
                    awal=akhir;
                }
            }
            tmp=  tmp*rate;
        }
        System.out.println("awal = "+awal);
        System.out.println("akhir = "+akhir);
        System.out.println("Jawaban: "+awal);
    }
    
    
    
}

    
