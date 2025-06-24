#include<stdio.h>
 
int main(void)
{
    int n[3] = {73, 95, 82};
    int sum = 0;
    for(int i=0;i<3;i++){
        sum += n[i];
}
 
switch(sum/30){
  case 10:
  case 9: printf("A");
  case 8: printf("B");
  case 7: 
  case 6: printf("C");
  default: printf("D");
}
    return 0;
}

// case가 성립한 뒤로 출력은 전부 나옴!! 기억할 것!