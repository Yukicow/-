

from random import *

answer = randint(1,4)

bal_list = [0,0,0,0]


show_list_max = 0

for i in range(0,3):

    show_list = randint(2,3)
    show_list_max += 1
    if show_list_max == 3:
        show_list = 2

    correct = 0
    loop = 1
    while(loop <= show_list):
        choice_list = randrange(0,4)
        if bal_list[choice_list] >= 2:
            continue
        print("{0}번 발모제".format(choice_list + 1))
        bal_list[choice_list] += 2
        if (choice_list + 1) == answer:
            correct += 1
        loop += 1

    if correct > 0:
        print("모발모발")
    elif correct == 0:
        print("No 모발스..")


    for x in range(0,4):
        if bal_list[x] >= 2:
            bal_list[x] -= 1
    

input_answer = int(input("정답을 입력해주세요"))


if input_answer == answer:
    print("정답입니다.")
else:
    print("틀렸습니다.")


