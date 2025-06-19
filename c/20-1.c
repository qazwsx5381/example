#include <stdio.h>

main() {
    int c=1;
    switch (3) { // switch문의 경우 break가 존재하지 않으면 case 3번부터 쭉 실행됨!!!
    case 1:c+=3;
    case 2:c++;
    case 3:c=0;
    case 4:c+=3;
    case 5:c-=10;
    default : c--;
    }
    printf("%d",c);
}