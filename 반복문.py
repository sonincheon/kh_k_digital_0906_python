## 반복문 : 조건이 참인 동안 계속 수행되는 구문
# n = int(input("정수를 입력 하세요 : "))
# sum = 0
# while n : # 0, non 만 "거짓" 이기에 나머지값은 "참"
#     sum += n
#     n -= 1  # 파이썬은 증감 연산자가 없음 .
# print(sum)

# while True :
#     age = int(input("나이를 입력하세요 : "))
#     if 0 < age < 200 :break
#     print("나이 입력 범위가 벗어 났습니다. ")


## for 요소 in 시퀀스 : 시퀀스의 각 요소를 순회하는데 사용(자바의 향상된 for분과 비슷)
# fruits = ["apple", "banana", "cherry",["seoul","korea"]]
# print(fruits[3][1][0])
# for e in fruits:
#     print(e[0])
#
# str1 = "서울시 강남구 역삼동 KH정보교육원"
# for e in str1 :
#     print(e, end= "/")


# # for 변수 in range(시작값, 종료값, 증감값)
# n = int(input("정수를 입력하세요 : "))
# sum = 0
# for i in range(1, n+1): # 1부터 n+1 미만 값까지 +1
#     sum += i
# print(sum)

## for문을 역순으로 반복하기
# for i in range(10, -1, -2): #  10부터 ~ -1 미만까지 출력 그래야 0이포함됨
#     print(i)
#
# # 이중 for문
# n = int(input("정수를 입력하세요 :" ))
# for i in range(0,n) :
#     for j in range(0,n) :
#         print("*", end=" ")
#     print()

# #구구단
# for i in range(2,10) : #2단 ~ 9단
#     for j in range(1,10) : # 1~ 10
#         print(f"{i} X {j}={i*j}")
#     print()

# # 홀짝 나누기
# n = int(input("정수 입력 : "))
# for i in range(0,n) :
#     for j in range(0,n) :
#         if j % 2 == 0 :
#             print("$",end=" ")
#         else:
#             print("*", end=" ")

# # nxn 숫자 찍기
# n = int(input("정수 입력 : "))
# for i in range(1,n*n +1) :
#     print(f"{i:3}",end=" ")
#     if i % n == 0 :
#         print()
#
# #1. 별찍기 (직삼각)
# n=int(input("별갯수 입력 : "))
# for i in range(n) :
#     for j in range(i+1) :
#         print("*",end=" ")
#     print()
#
#
# # 2 . 별찍기(역직삼각)
# n=int(input("별갯수 입력 : "))
# for i in range(n) :
#     for j in range(n-i) :
#         print("*",end=" ")
#     print()
#
#
# # 3. 별찍기 (반대 역직삼각)
# n=int(input("별갯수 입력 : "))
# for i in range(n) :
#     for j in range(n-i) :
#         if j % n == 0:
#              print("  "*i, end=" ")
#         print("*",end= " ")
#     print()
#
#
# # 4. 별찍기 ( 역 피라미드 )
# n=int(input("별갯수 입력 : "))
# for i in range(n) :
#     for j in range(n-i) :
#         if j % n == 0 :
#             print(" "*i, end=" ")
#         print("*",end= " ")
#     print()


# 문자와 ASCII 코드
# - chr : 유니코드 값을 입력 받아 그 코드에 해당하는 문자를 출력하는 함수
# - ord : 문자의 유니코드 값을 돌려주는 함수
for i in range(ord("A"),ord("Z")+1):
    print(chr(i), end=" ")     # chr 문자 출력
print()

for i in range(65,91):         # A:65 Z:90
	print(chr(i), end=" ")
print()



