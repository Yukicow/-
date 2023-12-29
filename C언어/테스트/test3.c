#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int Card[4][5]; // 같은 카드 경우 확인

int Animal_Card[4][5];// 보여주기 용

char *Animal[10]; //동물

int life = 25;

int Answer = 0;


int answer();

void Show_Card();

void Suffle_Card();

void Pick();



int main(void)
{
    srand(time(NULL));



    int input_num1;
    int input_num2;



    Animal[0] = "원숭이";
    Animal[1] = "하마";
    Animal[2] = "코끼리";
    Animal[3] = "호랑이";
    Animal[4] = "토끼";
    Animal[5] = "기린";
    Animal[6] = "박창수";
    Animal[7] = "거북";
    Animal[8] = "독수리";
    Animal[9] = "악어";



    for(int i =0; i < 4;i++){
        for(int j = 0; j < 5; j++){
            Card[i][j] = -1;
        }
    }
    Suffle_Card();
    


    
    while(1){
        Show_Card();
        printf("\n첫 번째 카드를 골라 주세요.");
        scanf("%d", &input_num1);
        if(Animal_Card[(input_num1-1)/5][(input_num1-1)%5] == 1 || ((input_num1 > 20) || (input_num1 < 1))){
            printf("\n다시 골라줘!\n");
            continue;
        }
        Pick(input_num1);


        printf("\n두 번째 카드를 골라 주세요.");
        scanf("%d", &input_num2);
        if(Animal_Card[(input_num2-1)/5][(input_num2-1)%5] == 1 || ((input_num2 > 20) || (input_num2 < 1))){
            Animal_Card[(input_num1-1)/5][(input_num1-1)%5] = 0;
            printf("\n다시 골라줘!\n");
            continue;
        }
        Pick(input_num2);


        if(Card[(input_num1-1)/5][(input_num1-1)%5] == Card[(input_num2-1)/5][(input_num2-1)%5])
            printf("\n정답!\n");
        else
        {
            Animal_Card[(input_num1-1)/5][(input_num1-1)%5] = 0;
            Animal_Card[(input_num2-1)/5][(input_num2-1)%5] = 0;
            printf("\n땡 틀렸당~\n");
        }

        life -= 1;
        printf("\n현재 남은 목숨 : %d개\n", life);


        if(answer() == 0)
            break;

        if(life <= 0){
        printf("=================");
        printf("\n   Game Over\n");
        printf("=================");
        break;
        }
    }

 

    return 0;


}




// 카드 랜덤 분배
void Suffle_Card(){

    for(int i = 0; i <10; i++){
        for(int j = 0; j<2; j++){
            int pos = rand() % 20;
            int x = pos/5;
            int y = pos%5;
            if(Card[x][y] == -1)
                Card[x][y] = i;
            else
                j--;
        }
    }
}


// 고르는 카드
void Show_Card(){
    int show_question = 1;
    for(int i = 0; i <4; i++){
        printf("\n");
        for(int j = 0; j <5 ; j++){
            if(Animal_Card[i][j] == 1)
                printf(" %5s", Animal[Card[i][j]]);
            else
                printf(" %5d", show_question);
            show_question += 1;
        }

        printf("\n\n");

    }
}



// 입력 받은 수를 동물 카드로 출력
void Pick(int num){
    num = num - 1;
    int x = num / 5;
    int y = num % 5;
    int answer = Card[x][y];
    Animal_Card[x][y] = 1;
    Show_Card();
}


int answer(){
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 5 ; j++){
            if(Animal_Card[i][j] == 0)
                return 1;
        }
    }
    printf("=================");
    printf("\n   Game Clear!\n");
    printf("=================");
    return 0;
}