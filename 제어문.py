# # 제어문이란 ? 조건문과 반보군을 의미하여 순차적인 흐름을 제어하는 목적으로 사용 된다.
# n = int(input("정수 입력 : "))
# if n > 100 :
#     print(f"{n}은 100보다 커요")
# elif n < 100 :
#     print(f"{n}은 100보다 작아요")
# else:
#     print("100과 같아요")


# 조건문에서 문자열 비교
while True :
    season = input("현재 계절을 입력 하세요 : ")
    if season == "spring" :
        print("봄")
        break
    elif season == "summer":
        print("여름")
        break
    elif season == "fall" or season == "autumn":
        print("가을")
        break
    elif season == "winter" :
        print("겨울")
        break
    else :
        pass
