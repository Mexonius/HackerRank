//  https://www.hackerrank.com/challenges/playing-with-characters/problem?h_r=next-challenge&h_v=zen

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int MAX_LEN=100;
    char c;
    char s[MAX_LEN];
    char sen[MAX_LEN];
    
    scanf("%c", &c); // take only one character
    printf("%c\n", c);

    scanf("%s", s); // take characters until the first white space
    printf("%s\n", s);
    
    /***
     * []   scanset character
     * ^\n  take input until a newline isn't encountered
     * %*c  reads the newline character and with the * that \n is discarded
     * */
    scanf("\n");  // because the previous scanf doens't take care about the \n char at the end of the 2nd line
    scanf("%[^\n]%*c", sen);
    printf("%s\n", sen);
    return 0;
}