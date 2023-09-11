# 크로저 : 함수(inner function)를 구현 하고 그 내부 함수를 반환하는 함수를 말합니다.
# def calc() :
#     a = 3 # 데이터 은닉
#     b = 5
#     def mul_add(x):
#         return a * x + b
#     return mul_add #내부 함수 리턴
#
# c = calc()
# print(c(1),c(2),c(3)) # 외부 함수의 변수의 값을 기억하고 있음

# import time
# def operation(x,y,callback) :
#     result = 0
#     for e in range (x) :
#         result += e+x+y
#         time.sleep(1)
#     callback(result)
#
# def collback(result) :
#     print(f"실행 결과를 되돌려 받기 위 한 콜백 함수 호출 : {result}")
#
# operation(10,20,collback)
#

#데코레이터 : 이미 만들어져 있는 함수의 앞과 뒤에 기능을 추가 할 떄 사용
from datetime import datetime
def datetime_deco(func) :
    def decorated():
      print(datetime.now())
      func()
      print(datetime.now())
    return decorated

@datetime_deco
def for_sum() :
    sum = 0
    for i in range(1,100+1):
        sum += i
    print(sum)

for_sum()