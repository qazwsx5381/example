#include <stdio.h>

int main()
{
    int n[5];
    int i;
    
    for(i=0;i<5;i++){
        printf("숫자를 입력하세요 : ");
        scanf("%d",&n[i]);
    }
    
    for(i=0;i<5;i++){
        // printf("%d",(가));
        printf("%d",n[(i+1) % 5]);
    }
 
    return 0;
}