# 파이썬 입력
# 사용자의 입력을 받아 그 값을 프로그램에서 사용하고자 할 떄 input() 함수를 사용
#input 함수를 통해서 입력 받은 데이터는 문자열로 반환 , 원하는 데이터형으로 변환이 필요

# print("이름을 입력 하세요 : ",end=" ")
# name = input()
# print(f"당신의 이름은 {name} 입니다.")

##간결하게
# name = input("이름을 입력하세요 : ")
# print(f"당신의 이름은 {name} 입니다.")
#
# age = int(input("나이를 입력하세요 : "))
# print(type(age)) # 타입 확인
# print(f"나이는 {age} 입니다.")
#
# addr = input("주소를 입력하세요 : ")
# jobs = input("직업을 입력하세요 : ")
# score = float(input("성적을 입력하세요 : "))
# print(f"""
# 안녕하세요? {name}님 \n
# 당신의 주소는 {addr}이고,직업은{jobs}이며,나이는{age}이며,성적은{score:2f}입니다.
# """)

##더 간결하게
# #split 함수의 기본은 공백 기준
# str1,str2 =input("이름과 주소 입력 : ").split()
# print(str1,str2)
# # 원하는 데이터형이 있을경우 map 사용
# kor,eng,mat=map(int,input("국어 영어 수학 : ").split())
# print(kor,eng,mat)

# val = list(map(int,input("성적 입력 : ").split()))
# print(val)

# hour, min , sec = map(int,input("시:분:초 :").split(":"))
# print(f"{hour}시 {min}분 {sec} 초 입니다.")

# 시간을 24시간제이며 : 기준으로 입력 받은 후 오전과 오후로 출력하도록 변경

hour, min , sec = map(int,input("시:분:초 :").split(":"))
if hour>12 :
    hour -=12;
    print(f"오후 {hour:02}시 {min:02}분 {sec:02} 초 입니다. ")
else:
    print(f"오전 {hour:02}시 {min:02}분 {sec:02} 초 입니다. ")




