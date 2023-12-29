


#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(void){

    char line[100];
    char contents[100];
    char password[20];
    char c;
    int i = 0;
    printf("비밀번호를 입력해 주세요");

    while(1){

        c = getch();

        if(c == 13)
        {
            password[i] = '\0';
            break;
        }
        else
        {
            printf("*");
            password[i] = c;
        }
        i++;
    }
    printf("\n=====비밀 번호 확인 중======\n\n");

    if(strcmp(password) == "quddtls123")
        printf("\n\n비밀번호 일치\n");

    char* fileName = "c:\\diary.txt";
    FILE* file = fopen(fileName, "a+b");


    if(file == NULL){
        printf("파일 열기 실패\n");
    }

    while(fgets(line,256,file) != NULL){
        printf("%s" ,line);
    }

    printf("내용을 계속 작성하세요! 종료하려면 EXIT를 눌러 주세요.\n");

    while(1){
        scanf("%s", contents);
    }


    return 0;
}