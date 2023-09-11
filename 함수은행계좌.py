
#계좌개설
def open_acount(name):
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name # 반환 값으로 이름을 전달

#입금 함수
def deposit(input) : # 잔고와 입금액을 매개변수로 전달 받음
    balance[0]+=input
    print(f"{input}이 입금 되었습니다. 잔액은 {balance[0]} 입니다.")

#출금 함수
def withdraw(output) :
    if balance[0] >= output :
        balance[0]-=output
        print(f"{output}이 출금되었습니다. 잔액은 {balance[0]}입니다.")
    else:
        print(f"출금한 금액이 부족 합니다.잔액은 {balance[0]}입니다.")

balance = [0] # 외부에서 선언했지만 매개변수로 전달하여 결과를 리턴으로 받음
name = open_acount("곰돌이사육사")
deposit(1000)
withdraw(500)
print(f"{name}의 잔액은 {balance[0]} 입니다")


