

import java.util.Scanner;
import java.io.IOException;

public class project {

    static int winner = 0;

    static int Game_going = 1;

    static int turn = 0;

    static int Pick;

    static char O = 'O';

    static char X = 'X';

    static char[][] Game_board = {{' ',' ',' '},{' ',' ',' '},{' ',' ',' '}};

    static int[][] Game_board_overlab = {{0,0,0},{0,0,0},{0,0,0}};
    
    static Scanner sc = new Scanner(System.in);

    static void Show_game(char[][] G_b){

        System.out.printf("%c |%c |%c\n", G_b[0][0],G_b[0][1],G_b[0][2]);
        System.out.printf("ㅡ+ㅡ+ㅡ\n");
        System.out.printf("%c |%c |%c\n", G_b[1][0],G_b[1][1],G_b[1][2]);
        System.out.printf("ㅡ+ㅡ+ㅡ\n");
        System.out.printf("%c |%c |%c\n", G_b[2][0],G_b[2][1],G_b[2][2]);

    }
    
    static int Ask(){
        
        System.out.println("원하는 위치를 입력해 주세요.\n");

        int Pick = sc.nextInt();

        return Pick;
    }

    static int End(int[][] board){

        int end_point = 0;
        for(int i = 0; i < 3; i++){
            for(int j = 0; j<3; j++){
                if(board[i][j] == 1 || board[i][j] == 2)
                    end_point += 1;
            }
        }
        if(end_point == 9){
            System.out.println("\n\n게임이 무승부로 끝났습니다.\n");
            return 0;
        }
        else
        return 1;

    }


    static int Winner(int[][] board){
        for(int i = 0; i < 3; i++){
            int win_O_point1 = 0;
            int win_O_point2 = 0;
            int win_X_point1 = 0;
            int win_X_point2 = 0;
            for(int j = 0; j<3; j++){
                if(board[i][j] == 1)
                    win_O_point1 += 1;
                if(board[i][j] == 2)
                    win_X_point1 += 1;
                if(board[j][i] == 1)
                    win_O_point2 += 1;
                if(board[j][i] == 2)
                    win_X_point2 += 1;
            }
            if(win_O_point1 == 3)
                return 1;
            if(win_O_point2 == 3)
                return 1;
            if(win_X_point1 == 3)
                return 2;
            if(win_X_point2 == 3)
                return 2;
        }
        for(int i = 0; i < 2; i++){
            int win_O_point3 = 0;
            int win_O_point4 = 0;
            int win_X_point3 = 0;
            int win_X_point4 = 0;
            for(int j = 0; j < 3; j++){
                if(board[j][j] == 1)
                    win_O_point3 += 1;
                if(board[2-j][2-j] == 1)
                    win_O_point4 += 1;
                if(board[j][j] == 2)
                    win_X_point3 += 1;
                if(board[2-j][2-j] == 2)
                    win_X_point4 += 1;
            }
            if(win_O_point3 == 3)
                return 1;
            if(win_O_point4 == 3)
                return 1;
            if(win_X_point3 == 3)
                return 2;
            if(win_X_point4 == 3)
                return 2;
        }
        return 0;
    }



    public static void main(String[] args) throws IOException {
        
        Show_game(Game_board);

        while(Game_going == 1){

            if(turn == 0) {
            Pick = Ask();
            Pick -= 1;
            int Pick_x_pos = Pick / 3;
            int Pick_y_pos = Pick % 3;
            if(Game_board_overlab[Pick_x_pos][Pick_y_pos] == 1 || Game_board_overlab[Pick_x_pos][Pick_y_pos] == 2) {
                System.out.println("이미 선점된 자리입니다.\n");
                continue;
            }
            else {
                Game_board[Pick_x_pos][Pick_y_pos] = O;
                Game_board_overlab[Pick_x_pos][Pick_y_pos] = 1;
            }
            turn += 1;
            Show_game(Game_board);
            }

            else {
            Pick = Ask();
            Pick -= 1;
            int Pick_x_pos = Pick / 3;
            int Pick_y_pos = Pick % 3;
            if(Game_board_overlab[Pick_x_pos][Pick_y_pos] == 1 || Game_board_overlab[Pick_x_pos][Pick_y_pos] == 2) {
                System.out.println("이미 선점된 자리입니다.\n");
                continue;
            }
            else {
                Game_board[Pick_x_pos][Pick_y_pos] = X;
                Game_board_overlab[Pick_x_pos][Pick_y_pos] = 2;
            }
            turn -= 1;
            Show_game(Game_board);
            }

            if(Winner(Game_board_overlab) == 1){
                System.out.println("\nO의 승리입니다.\n");
                break;
            }
            else if(Winner(Game_board_overlab) == 2){
                System.out.println("\nX의 승리입니다.\n");
                break;
            }

            Game_going = End(Game_board_overlab);

        }
        

    }
}
