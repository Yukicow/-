
class ero(Exception):
    def __init__(self,num1,num2):
        pass
    
    # def __str__(self):  
    #     return self.name


try:
    print("한 자리 수 나눗셈 계산기")
    num1 = int(input("숫자 입력"))
    num2 = int(input("숫자 입력"))
    if (num1 >=10) or (num2 >= 10):
        raise ero(num1, num2) 
    print("{0} % {1} = {2} 입니다.".format(num1, num2, int(num1/num2)))
    
except ero as err:
    print("10미만의 숫자를 입력해 주세요.")
    print(err)




