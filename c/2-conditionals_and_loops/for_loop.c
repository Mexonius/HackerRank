# https://www.hackerrank.com/challenges/for-loop-in-c/problem?h_r=next-challenge&h_v=zen

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
  	// Complete the code.
    for(int n=a; n<=b; n++) {
        if (n==1) {
        printf("one\n");
        }
        else if (n==2) {
            printf("two\n");
        }
        else if (n==3) {
            printf("three\n");
        }
        else if (n==4) {
            printf("four\n");
        }
        else if (n==5) {
            printf("five\n");
        }
        else if (n==6) {
            printf("six\n");
        }
        else if (n==7) {
            printf("seven\n");
        }
        else if (n==8) {
            printf("eight\n");
        }
        else if (n==9) {
            printf("nine\n");
        }
        else {
            printf(n%2==0 ? "even\n" : "odd\n");
        }
    }

    return 0;
}

