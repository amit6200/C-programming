#include<stdio.h>

int main()
{
    int a,b,c;
    printf("enter the value of a is\n");
    scanf("%d",&a);
    printf("enter the value of b is\n");
    scanf("%d",&b);
    printf("enter the value of c is\n");
    scanf("%d",&c);
   if(a<b||b<c||c<a)
   printf("the number is gretest");
 
    return 0;
}