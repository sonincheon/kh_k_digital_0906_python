# 값을 할당하는 방법
a = b = c = 1
print(a,b,c)

a,b,c = 1, False, "인천" # 여러개의 변수를 한번에 대입,
print(a,b,c)

# 타입 확인
# age = int(input("나이를 입력하세요 : "))
# print(type(age)) # type () 타입 확인

value = 0xffffff
print(value)

# 불리언 타입 : 참과 거짓의 값을 가짐
print(bool(1))      #참
print(bool(0))      #거짓
print(bool(-100))   #참
print(bool(""))     #거짓
print(bool(None))   #거짓, 값이 아직 정해지지 않았음을 의미
val =None

#문자열 타입 :
str1 = "Hello Python !!"
print(str1)
print(str1[0]) # 인덱싱
print(str1[2:5]) # 2번 인덱스에버 5번 인덱스 미확인
print(str1[2:])
print(str1*5)
print(str1 + " TEST")

#형변환 : 파이썬은 값이 할당되는 순간 형이 결정된, 이후 테이터형을 변경하고자할떄 형변형 사용
print(10+int("10"));
print("나이 : " + str(30))
print(1+3.141592+float("4.44"))


