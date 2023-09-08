# # 상근날드
# a = int(input())
# b = int(input())
# c = int(input())
# burger = [a, b, c]
# d = int(input())
# e = int(input())
# drink = [d,e]
# burger.sort()
# drink.sort()
# print(burger[0]+drink[0]-50)


# # 해답
# ls = list(map(int, input().split()))
# min_b = min(ls[:3])
# min_d = min(ls[3:5])
# print(f"{min_d + min_b - 50}")
#=================================================================================
# # 저항
# color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
# color = list(map(str,input("색을 선택해주세요 : ").split(",")))
# print((((color_list.index(color[0])*10))+(color_list.index(color[1])))*(10**color_list.index(color[2])))
#
#=================================================================================
# # pc방
# seat = []
# cnt = 0
# while True:
#     human = list(map(int, input("예약 자리 :").split()))
#     for i in human:
#         seat = i
#         if seat is not human:
#             cnt += 1
#             print(f"이미 예약된 자리입니다 . 누적 거절횟수 : {cnt}회 ")

# # 해답
# seat_num = list(map(int, input("예약 자리 :").split()))
# pc = [0]*100
# cnt = 0
# for e in seat_num :
#     if pc[e-1] != 0 :
#         cnt +=1
#     else:
#         pc[e-1] += 1
# print(f"이미 예약된 자리입니다 . 누적 거절횟수 : {cnt}회 ")



#=================================================================================
# 4번
a = list(map(str, input("문자 : ").split('-')))
b = []
for i in range(len(a)):
    b = a[i][:1]
    print(b, end="")

# 해답
upper_str = ""
for e in input() : # 입력 받는 개수만큼 자동 순회
    if e.isupper() : upper_str +=e
print(upper_str)