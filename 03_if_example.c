#include<stdio.h>

int main()
{
   int physics,chemistry,maths,biology;
   float total;
   printf("enter your physics marks\n");
   scanf("%d",&physics);
   printf("enter your chemistry marks\n");
   scanf("%d",&chemistry); 
   printf("enter your maths marks\n");
   scanf("%d",&maths);
   printf("enter your biology marks\n");
   scanf("%d",&biology);
   total=(physics+chemistry+maths+biology)/4;
   if((total<40)||physics<33||chemistry<33||maths<33||biology<33){
       printf("your total percentage is %f and you are fail\n",total);

   } 
   else{
       printf("your total percentage is %f and you are pass\n",total);
   }
    return 0;
}