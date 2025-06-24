#include<stdio.h> 
 
int main()
{
int m=4620;
int a,b,c,d;
// a=(가)
// b=(나)
// c=(다)
// d=(라)
a=m / 1000;
b=(m % 1000) / 500;
c=(m % 500) / 100;
d=(m % 100) / 10;
printf("1000원 개수: %d",a);
printf("500원 개수: %d",b);
printf("100원 개수: %d",c);
printf("10원 개수: %d",d);
return 0;
}