# 피타고라스의 정리
def veiw(a):
    if (a[0] ** 2) + (a[1] ** 2) == (a[2] ** 2):
        print("right")
    else:
        print("wrong")

num_list = []

while True:
    num = list(map(int, input("정수 입력 :").split()))
    num.sort()
    num_list.append(num)
    if num[0] == 0 and num[1] == 0 and num[2] == 0: break

for e in num_list:
    veiw(e)
