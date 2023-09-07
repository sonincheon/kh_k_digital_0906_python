# 산술연산자 : 사칙연산자( +,-,*,/) // 몫, ** 제곱연산자,%(나머지 연산자)

i = 10 # 값을 대입할떄 데이터형이 결정됨, 파이썬은 데이터형이 없음
j = 3
한글변수짓기 = "한글변수 입니다."
print(f"{i} + {j} = {i+j}")       # 더하기
print(f"{i} - {j} = {i-j}")       # 빼기
print(f"{i} * {j} = {i*j}") # 곱하기, 순서를 정할 수 있다.
print(f"{i} ** {j} = {i**j}")           # 제곱 연산자
print(f"{i} / {j} = {i/j:0.2f}")    # 나누기
print(f"{i} // {j} = {i//j}")     # 몫
print(f"{i} % {j} = {i%j}") # 나머지를 문자로 변경해서 출력

text = "Python!!!"
print(text + "Hello")
print(text * 3)
print(text + str(100))

print(f"증감연산자 시험 : {++i}")
i += 1 ## 파이썬은 증감 연산자가 없음
print(f"증감연산자 시험 : {i}")

## 간단 예제 : 파이썬은 변수를 상수로 만드는 방법은 없으며 , 관례상 변수 이름을 모두 대문자로 표시하면 상수로 간주
# TAX_RATE = 0.10
# income = int(input("당신의 수입은 얼마 입니까? "))
# print(f"당신이 내야할 세금은 {income * TAX_RATE:0.2f} 입니다.")

#관계연산자 : AND(&&) => and , OR(||) => or , 부정 ( ! )  => not

x = 10
y = 20
z = 30

rst1 = x > 0 and x > y #false
rst2 = x > 0 or x < y #true
rst3 = not((x > 0) or (x > y)) #false

print(rst1,rst2,rst3,sep="\t")

#다항 (3항) 연산자
num = int(input("정수입력 : "))
rst = (num %  2 == 0) and '짝수' or '홀수' # 참 or 거짓  // 람다식 e => (e % 2 == 0) and '짝수' or '홀수'
print(f"{num}은 {rst}입니다.")

#2진수 입력 받기 (0b) 0과 1
number =0b1010101
#8진수 입력 받기 (0o),0부터 숫자 7까지
number =0o1234575
#16진수 입력 받기(0x), 0123456789abcdef : 0부터 15까지
number =0xffff4ff




