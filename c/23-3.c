#include <stdio.h>
 
int main(void) {
int input = 101110;
int di = 1;
int sum = 0;
 
while (input > 0) {
// sum = sum + (input (가)(나) * di);
sum = sum + (input % 10 * di);
di = di * 2;
input = input / 10;
}
 
printf("%d", sum);
 
return 0;
}