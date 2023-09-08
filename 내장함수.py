# 내장함수 : 파이썬이 기본적으로 제공, import가 필요 없음

# 큰값 작은값 찾기
print(max(1,2,3,4,5,6,7,89,65,45))
print(min(1,2,3,4,5,6,7,89,65,45))

# 총 합 구하기
print(sum([1,2,3,4,5,6,7,100])) # 리스트
print(sum((1,2,3,4,5,6,7,100))) # 튜플
num =list(map(int,input("정수값 입력 : ").split()))
print(f"입력 받은 수의 총 합 : {sum(num)}")
print(f"입력 받은 수의 총 합 : {sum(num)/len(num)}") # 평균

# 몫과 나머지 구하기
print(f"몫과 나머지 : {divmod(10,4)}") # 튜플의 원리 튜플로 반환됨, 두개의 반환값으로 받음

#여러개의 값을 한번에 입력 받아 리스트로 만들기
#최대값 최소값, 합계, 평균
num1=list(map(int,input("정수 입력 : ").split()))
print(f"""
====================
최대값 :{max(num1)}
최소값 :{min(num1)}
합계 :{sum(num1)}
평균 :{sum(num1)/len(num1)}
몫과 나머지 : {divmod(sum(num1),5)}
====================
""")

#정렬
my_list = [1,1,2,31,3,132,1,2]
my_list.sort() # 오름차순
my_list.sort(reverse=True) # 내림차순
print(my_list)
print(sorted(my_list))
print(sorted(my_list,reverse=True))


