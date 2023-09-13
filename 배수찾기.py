# 배수찾기

def veiw () :
    n = int(input("정수 :"))
    list_num = list(map(int,input("수의 목룍 : ").split()))
    for e in list_num :
        if e %n == 0 :
            print(f"{e} is a multiple of {n}")
        else:
            print(f"{e} is NOT a multiple of {n}")

veiw()