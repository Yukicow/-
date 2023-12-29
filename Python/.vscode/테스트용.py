

from random import *


total = 0

def adding(num1):
        num1 = num1 + 1
        return num1

client_list = set([])



while True:
    

    complete_list = set([])

    client_num = randint(0,3)
    

    if (client_num == 0) & (client_list == set()):
        print("손님이 없네.")
        continue
    else:
        for client in range(0, client_num):  
            total = adding(total)
            client_list.add(total)
            continue

    print("{0} 번 손님 커피 준비 됐습니다.".format(client_list))
    while True:  
        try:
            if client_list == set():
                    break     

            c = int(input("커피 받기 : "))

            if not c in client_list:
                print("없는 번호에요.")
            elif c in client_list:
                complete_list.add(c)
                print("{0} 번 손님 커피 여깄습니다.".format(c))
                client_list = client_list - complete_list
        except ValueError:
            print("안 오나")
            break

    
