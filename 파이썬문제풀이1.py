# 1. 정해진 형식으로 시간을 입력받아서 출력하기
#  입력 형식 : 22 : 5 : 5 >> 오후 10시 05분 05초
from datetime import datetime

hour, min, sec = map(int, input("시간 : ").split(":"))

if hour > 12:
    hour -= 12
    print(f"오후 {hour:02}시 {min:02}분 {sec:02}초 입니다.")
else:
    print(f"오전 {hour:02}시 {min:02}분 {sec:02}초 입니다.")

# 2. 3개의 정수를 입력 받아 최대값과 최소 값 구하기

list1 = list(input("3개의 정숫값 :").split())
list1.sort()
num_max = list1[2]
num_min = list1[0]
print(f"최댓값 :{num_max},최솟값 :{num_min}")

# 3. 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
jumin = input("주민번호 : ")
current_year = datetime.today().year
gender = jumin[7]
year = jumin[:2]
month = jumin[2:4]
day = jumin[4:6]
old = int(current_year) - (1900 + int(year))
print(gender)
if gender == "1" or gender == "3":
    print(f"{year:02}년도{month:02}월{day:02}일,남자,{old}")
else:
    print(f"{year:02}년도{month:02}월{day:02}일,여자,{old}")

# 4.갯수가 정해지지 않은 여러개의 정수를 입력받아 평균구하기
num = list(map(int,input("정수 : ").split()))
print(f"총점 : {sum(num)}")
print(f"평균 : {sum(num)/len(num)}")

