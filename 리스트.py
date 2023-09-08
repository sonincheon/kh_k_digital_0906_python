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




