# 파이썬의 다양한 출력 방법
name = "손인천"
age = 15
gender = "남성"
job = "대학생"
addr = "서울시 관악구"

# c언어 스타일 : 서식지정자를 사용하는 방식
print("="*5, "C스타일", "="*5)
print("이름 : %s"%(name))
print("나이 : %d"%(age))
print("성별 : %s"%gender)
print("직업 : %s"%job)
print("주소 : %s"%addr)

# 파이썬 옛날 스타일 , 3.6 이전 (str.format)
print("="*5,"파이썬 스타일 1","="*5)
print("이름과 주소 : {}{}".format(name, addr))
print("나이 : {}".format(age))
print("성별 : {}".format(gender))
print("직업 : {}".format(job))
print("주소 : {}\n".format(addr))

# 파이썬 현재 스타일 : 3.6 이후방식( f와 {}로 사용 합니다.)
print("====== 파이썬 스타일 2 ======")
print(f"이름 : {name}")
print(f"나이 : {age}, 성별 : {gender}, 직업 : {job}")
print(f"주소 : {addr}\n")

# 자바 스타일 : 문자열 연결 방법 (+)
print("====== 자바 스타일 ======")
print("이름 : " + name)
print("나이 : " + str(age))
print("성별 : " + gender)
print("직업 : " + job)
print("주소 : " + addr)

#출력 시 정렬
# < - 좌측
# > - 우측 (기본값 : 생략 가능)
# ^ - 중앙
print("|{:5}|".format(10))  #우측 (기본값 생략됨)
print("|{:<5}|".format(10)) #좌측
print("|{:^6}|".format(10)) #중앙

#요즘스타일
print(f"|{10:5}|")  # 오른쪽 정렬, 10이라는 값을 오른쪽 정렬으로 출력 한다는 의미
print(f"|{10:<5}|") # 왼쪽 정렬, 10이라는 값을 왼쪽 정렬으로 출력 한다는 의미
print(f"|{10:^6}|") # 중간 정렬, 10이라는 값을 중간 정렬 한다는 의미
PI = 3.14159265334342
print(f"{PI:.4f}")