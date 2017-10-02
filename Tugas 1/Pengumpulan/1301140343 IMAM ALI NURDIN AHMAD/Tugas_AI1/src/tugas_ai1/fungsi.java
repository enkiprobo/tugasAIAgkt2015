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
public class fungsi {

    public double fungsiSA(double x1, double x2) {
        double fx = ((4 - (2.1 * (Math.pow(x1, 2))) + ((Math.pow(x1, 4)) / 3)) + (x1 * x2) + ((-4 + (4 * Math.pow(x2, 2))) * Math.pow(x2, 2)));
        return fx;
    }

    public double akurasi(double fa, double fr) {
        double ak = (1 - ((fa - fr) / fr) * 100);
        return ak;
    }
}
