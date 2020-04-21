// https://www.hackerrank.com/challenges/pointer-in-c/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function
    int s=*a+*b;
    int m=(*a-*b)>0?(*a-*b):(*b-*a);
    (*a)=s;(*b)=m;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}