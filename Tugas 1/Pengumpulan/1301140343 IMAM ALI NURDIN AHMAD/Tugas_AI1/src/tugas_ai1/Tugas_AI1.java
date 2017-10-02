/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tugas_ai1;

/**
 *
 * @author anzym
 */

import java.util.Random;
import java.util.Scanner;

public class Tugas_AI1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        fungsi fxx = new fungsi();
        final double temp = 0.9;
        double state = Double.MAX_VALUE;
        double T = 1000;
        double Tmin = 0.1;
        double x1 = 0, x2 = 0;
        
        System.out.println("\t x1 \t\t | \t\t x2 \t\t | \t fa");
        
        while (T > Tmin) {
            double x1min = -10; double x2min = -10; 
            double x1max = 10; double x2max = 10;
            double randx1 = x1min + (x1max - x1min) * new Random().nextDouble();
            double randx2 = x2min + (x2max - x2min) * new Random().nextDouble();
            
            double current = fxx.fungsiSA(randx1, randx2);
            
            if (current < state) {
                state = current;
                x1 = randx1;
                x2 = randx2;
            } else if (current > state) {
                double delta = current - state;
                if (Math.exp(-delta/T) > new Random().nextDouble()) {
                    state = current;
                    x1 = randx1;
                    x2 = randx2;
                }
            }
            T *= temp;
            System.out.println(x1 + "\t | \t" + x2 + "\t | \t" + state);
        }
        double fa = state;
        System.out.println("Input fr:  ");
        Scanner in = new Scanner(System.in);
        double fr = in.nextDouble();
        
        //System.out.println("Akurasi Model : " + fxx.akurasi(state, fr) + "%");
        
    }
}