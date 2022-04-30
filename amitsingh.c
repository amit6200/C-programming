#include<stdio.h>

int main()
{
    int physics,maths,english,hindi,chemistry;
    float total;
    printf("enter your physics marks\n");
    scanf("%d",&physics);
    printf("enter your maths marks\n");
    scanf("%d",&maths);
    printf("enter your english marks\n");
    scanf("%d",&english);
    printf("enter your hindi marks\n");
    scanf("%d",&hindi);
    printf("enter your chemistry marks\n");
    scanf("%d",&chemistry);
    total=(physics+maths+english+hindi+chemistry)/5;
    if(total<=70){
      printf("your total percentage is %f and you are fail\n",total);
    }
      else{
          printf("your total percentage is %f and you are pass\n",total   );
      }  
    return 0;
}