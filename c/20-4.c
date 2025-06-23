#include <stdio.h>
 
 main() {
   char *p="KOREA";
   printf("%s\n",p);
   printf("%s\n",p+3);
   printf("%c\n",*p);
   printf("%c\n",*(p+3));
   printf("%c\n",*p+2);
}

/*
%s\n = 문자열 끝이 0이 될때까지 출력
p+3 = R, printf("%s\n",p+3) = R 이후 문자열 출력
%c\n = 문자 하나의 값을 출력
*p = K | *(p+3) = E , *p에서 3칸 이동 | *p + 2 = M, 아스키코드로 변환 후 2를 더함(K의 아스키코드는 75)
*/