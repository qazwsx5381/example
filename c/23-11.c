#include<stdio.h>
int main(void){
int E[] = {64, 25, 12, 22, 11};
    int n = sizeof(E) / sizeof(E[0]);
    
    int i = 0;
    do {
        int j = i + 1;
        do {
 
            // if (E[i] (가) E[j]) {
            if (E[i] > E[j]) {
                int tmp = E[i];
                E[i] = E[j];
                E[j] = tmp;
            }
            j++;
 
       } while (j < n);
       
       i++;
    } while (i < n - 1);
    
return 0;
    
}