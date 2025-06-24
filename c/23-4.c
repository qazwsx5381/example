#include <stdio.h>
 
void swap(int* idx1, int* idx2) {
  
  int t = *idx1;
  *idx1 = *idx2;
//   *( 가 ) = t;
  *idx2 = t;
}
void Usort(int a[], int len) {
  for (int i = 0; i < len - 1; i++) {
    for (int j = 0; j < len - i - 1; j++) {
      if (a[j] > a[j + 1])
        swap(&a[j], &a[j + 1]);
    }
  }
 
  for (int k = 0; k < 5; k++) {
    printf("%d ", a[k]);
  }
}
 
int main(void) {
  int arr[] = {64, 34, 25, 12, 40};
  int nx = 5;
 
//   Usort(arr, (나));
  Usort(arr, nx);
  return 0;
}