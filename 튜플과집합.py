#튜플이란 ? 변경할 수 없는 시퀀스 자료형 입니다. ( 나머지는 리스트와 동일 )
# 튜플의 정의 () 괄호를 사용하거나 생략 할 수 있음

# #튜플 만들기
# person = "곰돌이사육사",20,"서울시 강남구 역삼동"
# print(person)
#
# #튜플 요소 접근 하기
# print(person[0])
# print(person[1])
#
# #튜플의 언패킹
# 이름, 나이, 주소 = person
# print(이름)
# print(나이)
# print(주소)

#튜플의 언패킹 기능을 이용한 함수 만들기
def get_person() :
    name = "가을"
    age = 23
    addr = "서울시 강남구 역삼동"
    return name, age, addr

result = get_person() #언패킹되서 전달되는 반환값을 패킹해서 받음
print(result)

a,b,c = get_person()
print(a)
print(b)
print(c)

tp =1,2,3,3,3,3,3
print(tp.count(3)) # 전달한 변수내의 갯수가 몇개인지 확인
print(tp.index(2)) # 매개변수의 변수 위치의 인덱스 확인
print(len(tp)) # 변수 갯수 확인

#튜플에서 안되는것 (이뮤터블 특성이기 떄문에 삭제할수없음)
# del tp[0]