# 홀수 짝수 리스트 나누기

# num_list=list(map(int,input("숫자를 입력하세요 : ").split()))
# hol_list=[]
# zak_list=[]
# for i in num_list :
#     if i % 2 ==0 :
#         zak_list.append(i)
#     else:
#         hol_list.append(i)
# print(f"홀 : {hol_list}")
# print(f"짝 : {zak_list}")

#map : 전달 받은 값을 함수 내부에서 가공해서 반환 ( 입력 개수와 반환 개수가 동일)
#filter : 전달 받은 값을 함수내부에서 조건에 일치하는 것만 골라서 반환

#람다식

num_list=list(map(int,input("숫자를 입력하세요 : ").split()))

hol_list = list(filter(lambda e: e % 2 != 0, num_list))
zak_list = list(filter(lambda e: e % 2 == 0, num_list))

print(f"홀 : {hol_list}")
print(f"짝 : {zak_list}")