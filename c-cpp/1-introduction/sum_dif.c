// https://www.hackerrank.com/challenges/sum-numbers-c/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
// https://www.codingcreativo.it/scanf/
// https://www.programiz.com/c-programming/c-arrays

#include <stdio.h>

int main()
{
    // int n1=0; int n2=0;
    // float m1=0.0; float m2=0.0;

    // scanf("%d %d",&n1,&n2);
    // printf("%d %d\n", n1+n2, n1-n2);
    // scanf("%f %f", &m1,&m2);
    // printf("%.1f %.1f\n", m1+m2, m1-m2);

    int n[2];
    float m[2];

    scanf("%d %d", &n[0],&n[1]);
    printf("%d %d\n", n[0]+n[1], n[0]-n[1]);
    scanf("%f %f", &m[0],&m[1]);
    printf("%.1f %.1f", m[0]+m[1], m[0]-m[1]);
    
    return 0;
}