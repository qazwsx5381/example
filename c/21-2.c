#include <stdio.h>
int main(){
   int res;
   res = mp(2,10);
   printf("%d",res);
   return 0;
}
 
int mp(int base, int exp) {
   int res = 1;
   for(int i=0; i < exp; i++){
      res *= base;
   }
   
   return res;
}

/*
mp 선언은 base의 exp승울 구하는 것
*/