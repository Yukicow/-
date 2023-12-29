#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main(void){

    char a[4];

    char b[3];


    // scanf("%s", b);
    


    fgets(a, sizeof(a), stdin);
    getchar();

    scanf("%s", b);
    

    printf("%s , %s", a,b);

    return 0;
}