#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main(int argc, char* argv[]) 
{
         //Checking for correct number of command line arguments
         if (argc == 4) {         
             // ax^2 + bx + c = 0 where arg1 = a arg2 = b etc
             //Conversion of cmd arguments to ints
             int a = atoi(argv[1]), b = atoi(argv[2]), c = atoi(argv[3]);
             //Finding the Discriminant and checking the number of roots in the real domain
             if (a == 0)
                printf("You're a grown ass man, solve the linear equation");
             else {
                 int dDiscriminant = b*b -4*a*c;
                 if (dDiscriminant >= 0) {
                               //At least one solution
                               double dX1 = (b*(-1) + sqrt(dDiscriminant))/(2*a);
                               double dX2 = (b*(-1) - sqrt(dDiscriminant))/(2*a);
                               if  (dX1 == dX2)
                                   printf("X = %f\n", dX1);
                               else
                                   printf("x1 = %f, x2 = %f\n", dX1, dX2);
                                   }
                 else
                     printf("Rip bozo idk how to use complex numbers yet");
                 };
             }
         else
             printf("Incorrect number of arguments. If a power of x is not present, use 0 in the appropriate position\n");
         system("Pause");
}      

                               
