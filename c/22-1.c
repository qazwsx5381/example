#include <stdio.h>
#include <stdlib.h>

int func(int a)
{
    if (a <= 1)
        return 1;
    return a * func(a - 1);
}

int main()
{
    int a;
    scanf("%d", &a);
    printf("%d\n", func(a));
    printf("%s\n", "test입니다.");
    system("pause");
    return 0;
}