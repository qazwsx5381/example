#include <stdio.h>
void main(){
struct insa {
	char name[10];
    int age;
    }
    a[] = {"Kim",28,"Lee",38,"Park",42,"Choi",31};
    struct insa *p;
    p = a;
    p++;
    printf("%s\n", p-> name);
    printf("%d\n", p-> age);
}

/*
struct insa a[] = {...}	구조체 배열 선언 및 초기화
struct insa *p = a;	구조체 포인터가 배열의 첫 번째 요소를 가리킴
p++;	다음 구조체 요소(a[1])를 가리킴
p->name	"Lee" 출력
p->age	38 출력
*/