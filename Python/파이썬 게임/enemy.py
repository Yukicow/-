
import pygame

from random import *


pygame.init()


# 스크린

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width ,screen_height))


#  이미지 로드

background = pygame.image.load("C:\\Users\\user\\Desktop\\나의 코딩\\파이썬 게임\\이미지들\\배경.png")

character = pygame.image.load("C:\\Users\\user\\Desktop\\나의 코딩\\파이썬 게임\\이미지들\\캐릭터.png")

character_right = pygame.image.load("C:\\Users\\user\\Desktop\\나의 코딩\\파이썬 게임\\이미지들\\오른쪽.png")

character_left = pygame.image.load("C:\\Users\\user\\Desktop\\나의 코딩\\파이썬 게임\\이미지들\\왼쪽.png")

weapon = pygame.image.load("C:\\Users\\user\\Desktop\\나의 코딩\\파이썬 게임\\이미지들\\총알.png")


# 프레임

clock = pygame.time.Clock()


# 잡것들

total = 0

running = True

score_font = pygame.font.Font(None, 40)


# 무기

weapon_x = 0
weapon_y = 0

weapon_cool = 1

now_cool = 0

weapons = []


# 똥

class Enemy():

    def __init__(self):
        self.image = pygame.image.load("C:\\Users\\user\\Desktop\\나의 코딩\\파이썬 게임\\이미지들\\똥.png")
        self.x_pos = 10
        self.y_pos = 20
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.width = self.size[0]
        self.height = self.size[1]
        self.speed = 10
        # self.remove = -1

    def load_enemy(self):
        self.speed = (randint(2,6)/10)
        self.x_pos = randint(0,(480-self.width))    
        self.y_pos = -randint(100,400)
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos

    def draw_enemy(self):
        screen.blit(self.image, (self.x_pos,self.y_pos))

    def update_rect(self):
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos


enemys = []

for i in range(0,6):
    enemy = Enemy()
    enemy.load_enemy()
    enemys.append(enemy)






# 캐릭터 생성


go_left = False

go_right = False


character_size = character.get_rect().size

character_width = character_size[0]
character_height = character_size[1]

character_rect = character.get_rect()

character_x_pos = (screen_width / 2) - character_width

character_y_pos = (screen_height - character_height)


while running:
    


    cool_down = pygame.time.get_ticks() / 1000


    score = score_font.render(str(int(total)), True,(0,0,255))

    to_x = 0

    dt = clock.tick(60)

    screen.blit(background, (0,0))


    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
        # 캐릭터 움직이기

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                go_left = True
            if event.key == pygame.K_RIGHT:
                go_right = True
            if event.key == pygame.K_z:
                if cool_down > now_cool:
                    now_cool = cool_down + weapon_cool
                    weapon_x = character_x_pos + 20
                    weapon_y =character_y_pos
                    weapons.append([weapon_x,weapon_y])




        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                go_left = False
            if event.key == pygame.K_RIGHT:
                go_right = False

        

                
    
    if character_x_pos <= 0:
        go_left = False

    if character_x_pos >= (screen_width - character_width):
        go_right = False



    if go_left == True:
        to_x -= 3

    if go_right == True:
        to_x += 3

    character_x_pos += to_x

    for q in weapons:
        if q[1] > 0:
            q[1] -= 0.7 *dt


 

    #무기 위치

 




    # 캐릭터 충돌 위치

    character_rect.left = character_x_pos
    character_rect.top = character_y_pos



    for x in range(0,len(enemys)):
        enemys[x].draw_enemy()
        enemys[x].y_pos += enemys[x].speed * dt
        enemys[x].update_rect()
        if enemys[x].y_pos > 640:
            enemys[x].load_enemy()
            total += 1

    # 충돌 처리

    for y in range(0,len(enemys)):
        if character_rect.colliderect(enemys[y].rect):
            print(f"점수 : {total}점")
            running = False
        

    

    for weapon_index, weapon_val in enumerate(weapons):
        weapon_x = weapon_val[0]
        weapon_y = weapon_val[1]

        weapon_rect = weapon.get_rect()
        weapon_rect.left = weapon_x 
        weapon_rect.top = weapon_y
        if weapon_val[1] < 0:
            del weapons[weapon_index]
        for enemy_index, enemy_val in enumerate(enemys):
            if weapon_rect.colliderect(enemys[enemy_index].rect):
                del weapons[weapon_index]
                del enemys[enemy_index]
                a = Enemy()
                a.load_enemy()
                enemys.append(a)
                total += 1



    # 스크린에 출력

    if ((go_right == False) and (go_left == False)) or ((go_right == True) and (go_left == True)): 
        screen.blit(character, (character_x_pos,character_y_pos))
    if go_right == True: 
        screen.blit(character_right, (character_x_pos,character_y_pos))
    if go_left == True: 
        screen.blit(character_left, (character_x_pos,character_y_pos))
    
    for weapon_x, weapon_y in weapons:
        screen.blit(weapon, (weapon_x,weapon_y))


    screen.blit(score, (10,10))
    
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos


    pygame.display.update()




pygame.quit