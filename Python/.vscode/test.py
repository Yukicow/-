

from xml.dom import HIERARCHY_REQUEST_ERR


answer = input("Input the answer : ")

heart = 10

letters = ""


while True:


        succeed = True

        letter = input("Input letter : ")
        print()
        if letter in answer:
                print("Correct")
        elif not letter in answer:
                print("Wrong")

        letters += letter

        for i in answer:
                if i in letters:
                        print(i, end = "")
                else:
                        print("_", end = "")
                        succeed = False


        if succeed:
                print("\nsuccess")
                break
  

        if not letter in answer:
                heart -= 1


        if heart <= 0:
                print("\nGame over")
                break
                