from datetime import datetime

print(38)  #정수
print("문자열")  #문자열
print([1,2,3])  #리스트
print(1+3)
print("파"+"이"+"썬")  # 문자열 이어붙이기, (정수 + 문자열 적용 x)print(1+"3")
print("파""이""썬")
print("파","이","썬")  # , 구분자 (한칸 공백을 가지고 있음)
print("파\n\n\n이\t\t썬")  # \n : 줄바꿈  \t : 탭 (4칸띄우기)

print("""
 이 구간은 
출력 구간 입니다.
""")

print("안녕하세요 라고 \"곰돌이사육사가\" 말했습니다. ")

# end 와 sep 옵션
# end : 출력문에서 끝에 자동으로 삽입되는 문자를 지정하는 옵션 : \n
print("Hello", end="\n") #자동으로 줄바꿈이 포함되어있음
print("Hello", end=" ") # 줄바꿈없이 띄어쓰기
print("Hello", end="*") # 끝자리에 * 붙여넣음
print()

# sep : 출력문의 중간에 삽입되는 문자를 지정하는 옵션 : 기본은 space
print("life","is","too","short", sep="/") #단어 사이에 /를 넣음, /n넣으면 줄바꿈
print("life","is","too","short", sep="\n")
print("life","is","too","short", sep="\\")
print("010","9118","4894",sep="-")
year = 2023
month = 9
day = 6
print(year,month,day,sep="/") # 2023/9/6

current_year =datetime.today().year
print(current_year)
