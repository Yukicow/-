

from random import *

import pygame


pygame.init()


clock = pygame.time.Clock()

# 원하는 화면 크기 지정
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height)) # 파이썬 화면 크기 설정


pygame.display.set_caption("코미 게임") # 게임 이름 지정


running = True # 게임이 꺼지지 않고 유지하게 만들기 위한 변수.


# 이미지 불러오기
background = pygame.image.load("C:\\Users\\user\\Desktop\\나의 코딩\\파이썬 게임\\이미지들\\배경.png")

character = pygame.image.load("C:\\Users\\user\\Desktop\\나의 코딩\\파이썬 게임\\이미지들\\캐릭터.png")

character_right = pygame.image.load("C:\\Users\\user\\Desktop\\나의 코딩\\파이썬 게임\\이미지들\\오른쪽.png")

character_left = pygame.image.load("C:\\Users\\user\\Desktop\\나의 코딩\\파이썬 게임\\이미지들\\왼쪽.png")



character_size = character.get_rect().size # 이미지 크기 구하기 rect 는 rectengle 직사각형 이라는 뜻.



# 캐릭터 사이즈 정하기
character_width = character_size[0]
character_height = character_size[1]




# 캐릭터 생성 위치
character_x_pos = (screen_width/2) - (character_width/2) # 좌표는 0,0 기준으로 왼쪽 끝 맨 위이기이다.
character_y_pos = (screen_height) - character_height # 생성 위치 기준으로 오른쪽 밑으로 생성됨.


# 폰트
game_font = pygame.font.Font(None, 40)


# 이동


to_right = False
to_left = False

speed = 0.3


# 총 시간
total_time = 11


 # True 는 안티앨리어싱 이라는 건데 대각선을 부드럽게 출력하는 지에 대한 여부.



while running:

    dt = clock.tick(60) # 프레임당 한 번 호출되며 이전 호출보다 얼마나 지났는 지를 밀리초 단위로 반환.
    # () 안에 인수를 전달하면 함수는 게임이 초당 인수 보다 느리게 실행되도록 지연된다. 게임의 런타임 속도를 제한하는 데 도움이됩니다. 
    # 프레임 당 한 번 Clock.tick(60) 을 호출 하면 프로그램은 초당 60 프레임을 초과하여 실행되지 않습니다.


    # 시작 시간
    start_time = pygame.time.get_ticks()/1000

    timer = game_font.render(str(int(total_time - start_time)),True , (0,0,255))
    
    # 시간 초과

    if (total_time - start_time) < 0:
        print("게임 승리")
        running = False


    for event in pygame.event.get(): # 어떤 이벤트가 발생하면 그 값을 get()이 받고 그 이벤트에 대한 값을 event에 넣음 매 순간 인식하는 개념이 아님. 이벤트 발생 때만 반복
        if event.type == pygame.QUIT: # x 버튼을 누르면 -> x를 누르는 순간 이벤트 i에 대해 Quit으로 인식되는 것. 
            running = False
    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            elif event.key == pygame.K_RIGHT:
                to_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            elif event.key == pygame.K_RIGHT:
                to_right = False


    to_x = 0

    if (character_x_pos <= 0):
        to_left = False

    if ((character_x_pos + character_width) >= screen_width):
        to_right = False            


    if to_right == True:
        to_x += speed

    if to_left == True:
        to_x -= speed


    if to_right == False:
        to_x += 0

    if to_left == False:
        to_x -= 0


    character_x_pos += to_x * dt # dt를 곱해주면 프레임에 상관없이 비슷한 속도를 가짐 dt의 값이 뭔지 알면 이해 될 거임.
    

    # 캐릭터 위치 업데이트 하기
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos




    # 충돌 체크

   
    # 적 생성
        


 

    # screen.fill((0,0,255)) 이건 RGB 기준으로 색상을 지정해 화면을 채우는 것.

    screen.blit(background, (0,0)) # 화면에 이미지 전송하기

    if to_left == True:
        screen.blit(character_left, (character_x_pos, character_y_pos))

    elif to_right == True:
        screen.blit(character_right, (character_x_pos, character_y_pos))

    else:
        screen.blit(character, (character_x_pos, character_y_pos))



    # 참고로 blit이라는 것은 전에 출력 됐던 내용도 남는다. 하지만 아닌 것 처럼 보여지고 있는데.
    # 이는 백그라운드 이미지가 있기 때문이다. 다시 루프를 반복할 때 생생되는 이미지들로 전에 있던 이미지가 가려지는데
    # 백그라운드는 화면 전체를 가리기 때문에 마치 전에 있던 것들이 없어진 것 처럼 보이는 것 뿐이다.
    # 실제로는 배경 뒤에 이미지들은 남아 있다.
 
    screen.blit(timer, (10,10))

    pygame.display.update() # 이벤트를 매순간 새로 인식하기 때문에 그 순간마다 이벤트를 업데이트 해줄 필요가 있음.


    

    

pygame.quit()