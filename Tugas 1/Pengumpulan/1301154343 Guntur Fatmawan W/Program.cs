using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TuProo
{
    
        class Program
        {
			static double fungsi (double x1, double x2){
				return (((4 - (2.1 * Math.Pow(x1, 2)) + (Math.Pow(x1, 4) / 3)) * Math.Pow(x1, 2)) + (x1 * x2) + ((-4 + 4 * Math.Pow(x2, 2)) * Math.Pow(x2, 2)));
			}
            static readonly Random random = new Random();
            static double generate(double start, double end)
            {
                var rand = random.NextDouble();
                return start + (rand * (end - start));
            }

            public static void Main(string[] args)
            {
                double current1, current2, new1, new2, best1, best2;
                double t, counter, probabilitas, teta;
                double fcurrent, fnew, fbest;


                current1 = 3; current2 = 2;
                best1 = 0; best2 = 0;
                fbest = 0; 
                counter = 1;


                t = 10000000;

                while (t > 0.0000000001)
                {
                    
                    new1 = generate(-10, 10);
                    new2 = generate(-10, 10);
                    fcurrent = fungsi(current1, current2);
                    fnew = fungsi(new1, new2);

                    if ((fnew - fcurrent) < 0)
                    {
                        current1 = new1; current2 = new2;
                        best1 = new1; best2 = new2;
                        fbest = fnew;
                    }
                    else
                    {
                        probabilitas = Math.Exp(-((fnew - fcurrent) / t));
                        teta = generate(0, 1);
                        if (teta < probabilitas)
                        {
                            current1 = new1; current1 = new2;
                        }
                    }
					counter=counter+1;
                    if (counter == 66)
                    {
                        t = 0.999 * t;
                        counter = 1;
                    }


                }
                Console.WriteLine(fbest.ToString("F6"));
                Console.ReadKey(true);
            }
        }
}