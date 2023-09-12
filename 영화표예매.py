# - 메뉴는 [1]예매하기, [2]종료하기
# - 사용자로부터 좌석번호(index)를 입력받아 예매하는 시스템이다. (좌석은 10개이다.)
# - [V] [V] [V] [  ] [  ] [  ] [  ] [  ] [  ] [  ]
# - 예매가 완료되면 해당 좌석 값을 1로 변경한다.
# - 이미 예매가 완료된 좌석은 재구매할 수 없다.
# - 한 좌석당 예매 가격은 12000원이다.
# - 프로그램 종료 후, 해당 영화관의 총 매출액을 출력한다.

seat = [0] * 10
cnt = 0

def print_seat() :
    for e in seat :
        if e==0 : print("[ ]", end=" ")
        else: print("[v]", end=" ")
        print()

while True :
    menu = int(input("[1]예매하기 [2]종료하기: "))
    if menu == 1 :
        print_seat()
        seat_num = list(map(int,input("좌석을 선택해주세요(1~10)").split()))
        for e in seat_num :
            if seat[e-1] == 0 :
                cnt+=1
                seat[e-1] +=1
                print(f"{e}번 좌석 구매가 완료되었습니다.")
            else:
                print("이미 판매된 좌석입니다.")
    elif menu ==2 :
        print(f"총 매출은 {cnt*12000}원 입니다.")
        break
    else:
        print("메뉴를 다시 입력하세요.")