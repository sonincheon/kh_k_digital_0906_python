# 크기가 정해지지 않은 요소들에 대해 값을 저장하기 위한 자료형
# 아무 자료형으로 와도 된다.
# 중첩 사용 가능 [ [],[],[],[], [[[ ]]] ]
# 뮤터블 객체 ( 읽고, 쓰기가 가능)

number = [1,2,3,4,5,6]
fruits = ["애플","바나나","오렌지"]
mixed = [1, True, "seoul",12.5454]
dup = [[1,2,3,4,5],["애플","바나나"]]

# #변수와 리스트를 비교
# kor, eng, mat = map(int, input("성적입력 : ").split())
# print(sum([kor,eng,mat]))
#
# # 리스트는 성적의 개수에 상관없이 입력 받을 수 있음
# score = list(map(int, input("성적입력 : ").split()))
# print(sum(score/len(score)))

str_name = ["seoul","gangnam","suwon","incheon"]
print(str_name)
print(str_name[1])
print(str_name[1][2]) # 1번의 겹치는 수 출력
# 슬라이싱
slice =str_name[1:3]
print(slice)
print(len(slice[0]))
print("===================")
primes = [2,3,5,7]
print(primes[0])
print(primes[-1])
print(primes[-2:])

print("===================")
# 리스트 연산자 : 연결(+),반복(*), len()
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a +list_b)
print(list_a * 3)
print(len(list_a+list_b))

print("===================")
# 리스트 요소 추가하기 : append() : 리스트 뒤에 추가 , isert(index, 값) : 해당 인덱스에 값을 삽입
list_a = [1,2,3]
list_a.append(4)
list_a.append(5)
list_a.insert(1,10) # 1번배열 에 10 추가
print(list_a)

print("===================")
#리스트 제거하기 : pop(), remove(), clear(), del 리스트명 [인덱스]
#pop() : 인덱스가없으면 마지막 인덱스의 값을 반환하고 삭제
#        인덱스가 있으면 해당위치의 값을 삭제
#remove(값) : 해당하는 값을 제거, 만약 동일한 값이 여러개인 경우 낮은 인덱스 값 제거
#clear() : 모든 값을 삭제, 리스트는 지우지 않음( 빈리스트로 남는다 )
list_all= [1,2,3,4,5,6,7,8,9,1,2,3,4,"a","b"]
print(list_all.pop()) #마지막 인덱스 반환하고 삭제
print(list_all)
print(list_all.pop(8)) # 해당 인덱스의 값을 삭제하면서 보여줌 (반환하고 삭제)

list_all.remove(2) # 리스트에 해당하는 값을 제거하지만 보여주지않음 (반환값 x)
print(list_all)

del list_all[3] # 해당 인덱스의 값을 지움
print(list_all)

list_all.clear()
print(list_all)

# 중복 제거
my_list = [1,1,2,3,4,5,4,4,3]
new_list=[]
for e in my_list :
    if e not in new_list :
        new_list.append(e)
print(new_list)

# map(반환 함수 , 입력자료형), filter(반환함수, 입력 자료형) 동작 확인
# num = list(map(lambda e:int(e)*int(e),input("값 : ").split()))
# print(num)

# num1 = list(filter(lambda e:int(e)%2==0,input("값 : ").split()))
# print(num1)

#리스트의 원소 스캔하기
x = ["존","조지","폴","링고"]
for e in x : #향상된 포문
    print(e)
for i in range(len(x)) : # 범위 기반 for 문 (초기값, 최종값, 증강값)
    print(x[i])












