#include<stdio.h>

int main()
{
    int ratting;
    printf("enter your (1-3)");
    scanf("%d",&ratting);
    switch(ratting){
    case 1:  
    printf("your ratting is 1");
    break;
    case 2:
     printf("your ratting is 2");
     case 3:
     printf("your ratting is 3");
    }
    return 0;
}