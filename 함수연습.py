# # 함수란 ? 특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램
# # 이름 , 주소 , 전화번호를 매개변수로 전달받아
# def name_card(name, addr, phone):
#     print(f"""주소 {addr}
# 전화번호 {phone}
# 이름 {name}
# 회사 : Kh정보교육원""")
#
#
# # 함수는 선언이후 호출 해야만 동작 함, 한번 만들어진 함수를 여러번 호출하여 반복되는 코드를 줄임
# name_card("안유진", "서울시 강남구", "010-5454-5959")
# name_card("장원영", "서울시 관악구", "010-2121-2333")
# name_card("홍길동", "부산시 서구", "010-9898-7777")

# 순차 검색
# def search_list(a, x ) :
#     for i in range (len(a)) :
#         if x == a[i] : return i
#     return -1
#
# v = [17,92,18,33,58,7,33,42]
# print(search_list(v,33))
# print(search_list(v,18))
# print(search_list(v,100))

# 기본값 인자 : 함수 선언 시 매개변수에 대해서 기본값을 정의 할 수 있습니다 .
# 매개변수에 기본값이 정의 되어 있는 경우 함수 호출시 인자값을 넣지 않으면 기본값을 호출 됨
def profile(name, year=2, age=18, school="태양고"):
    print(f"이름 : {name},학교 : {school}, 학년 {year},나이 : {age}")

profile("나희도")
profile("고유림")
profile("백이진",None,22)

#가변 매개변수 : 변수의 개수가 정해지지 않은 경우에 사용,
# * (별표)를 붙여주면 함수의 매개변수를 몇개를 입력하든 함수내에서
# def profile(name, age,*lang) :
#     print(f"이름 : {name}, 나이 :{age}",end=" ")
#     for e in lang :
#         print(e,end= " ")
#     print()
#
# profile("나희도",18,"Python","Java","C","C++")

knife =10 #칼 10자루 준비
def game(player, knife) :
    knife -= player
    print(f"남아 있는 칼은 {knife}입니다.")
    return knife

player =int(input("경기에 참여 하는 학생이 몇명 입니까 "))
knife = game(player, knife)
print(f"경기에 사용하고 남은 칼은 {knife}입니다")



