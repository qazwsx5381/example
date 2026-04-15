#include <stdio.h>
int cnt = 0;
int f1(int);

int main () {
    int k;
    f1(5);
    printf("%d", cnt)
}
int f1(int n){
    if (n==0) {
        return 0;
    }
    if(n==1){
        cnt++;
        return 1;
    }
    return(f1(n-1)+f1(n-2));
}