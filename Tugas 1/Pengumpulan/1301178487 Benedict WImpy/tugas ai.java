import java.lang.Math; // headers MUST be above the first class
import java.util.Random;

// one class needs to have a main() method
public class HelloWorld
{
  // arguments are passed using the text field below this editor
  public static void main(String[] args)
  {
	 double hasilm, temperature= 1000, chill=0.999, goal=1; 
     int nomor,nomorberhasil;
	 float xsatu,xdua,xsatum,xduam;
	 double selisih = 100, probabilitas = 0 ,nrandom;
	 
	 nomorberhasil=1000;
	 nomor=1;
	 xsatum=11;
	 xduam=11;
	 hasilm=99999999;
     double empat = 4;
    	double dua = 2;
		
	System.out.println("----------------------------");
	System.out.println("Nama : Benedict Wimpy ");
  	System.out.println("NIM  : 1301178487 ");
  		
	while (temperature>=goal)
  	{	float min = -10;
		float max = 10;
		Random rand = new Random();
		xsatu = rand.nextFloat() * (max - min) + min;
 		xdua = rand.nextFloat() * (max - min) + min;
 		
    	 
		double xsatupangkatempat = Math.pow(xsatu, empat);
  		double xsatupangkatdua = Math.pow(xsatu, dua);
  		double xduapangkatdua = Math.pow(xdua, dua);
  		
  		double dalamkurung = 4-(2.1 * xsatupangkatdua)+(xsatupangkatempat/3) ;
    	double lanjutan = (dalamkurung*xsatupangkatdua) +(xsatu*xdua)+((-4 +(4*xduapangkatdua))*xduapangkatdua);	 
    	
		if( lanjutan < hasilm)
		{
			xsatum=xsatu;
			xduam=xdua;
			hasilm=lanjutan;
			nomorberhasil=nomor;
			
            System.out.println( "iterasi ke =" +nomorberhasil);
     		System.out.println("x1 = " + xsatu);
  		    System.out.println("x2 = " +xdua);
  		    System.out.println("hasil sementara = "+lanjutan);
  		    System.out.println("----------------------------");
  		    System.out.println(" ");
  		    
		}
		
		else
		{
		   
            selisih =lanjutan-hasilm;
            probabilitas = 1/(Math.exp(selisih/temperature));
            
            double minprob = 0.01;
		    float maxprob = 1;
	 	    Random rando = new Random();
		    nrandom = rando.nextFloat() * (maxprob - minprob) + minprob;
            	
            	
            if(probabilitas > nrandom)
            {
                xsatum=xsatu;
                xduam=xdua;
                hasilm=lanjutan;
                System.out.println( "iterasi ke =" +nomor);
                System.out.println("x1 min = " + xsatum);
  		        System.out.println("x2 min = " +xduam);
  		        System.out.println("temp = " + temperature);
                System.out.println("sel = " + selisih);
                System.out.println("prob = " + probabilitas);
                System.out.println("nilai random = " + nrandom);
                System.out.println("Hasil sementara = " +hasilm);
                System.out.println("----------------------------");
  		        System.out.println(" ");
            }
        }
		
	
		
		nomor++;
		temperature=temperature*chill;
	}
		
		System.out.println("x1 min = " + xsatum);
  		System.out.println("x2 min = " +xduam);
  		System.out.println( "hasil minimal =" +hasilm);
  		System.out.println( "iterasi ke =" +nomorberhasil);
    
  }
   

}