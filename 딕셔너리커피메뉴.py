menu_dic = {
    #메뉴이름 : [ 카테고리, 가격 , 설명]
    "Americano": ["Coffee", 2000, "기본 커피 입니다."], # 키와 값으로 구성되며 , 값을 리스트로 만들어 여러가지 저보를 포함 시킴
    "Espresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MilkTea": ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}

while True :
    print("메뉴를 선택 하세요.")
    menu = input("[1] 메뉴 보기, [2] 메뉴 조회, [3] 추가 하기, [4] 삭제 하기, [5] 종료 하기 : ") # input 기본 문자열로 반환됨
    if menu == "1":
        for key in menu_dic :
            print(key,":",menu_dic[key])

    elif menu == "2":
        rtrv_name = input("조회 할 메뉴를 입력하세요 :")
        if rtrv_name in menu_dic :
            print(menu_dic[rtrv_name])
        else:
            print("찾는 메뉴가 없습니다.")

    elif menu == "3":
        add_menu = input("추가할 메뉴를 입력하세요 : ")
        if add_menu not in menu :
            category = input("카테고리 입력 : ")
            price = int(input("가격 입력 :"))
            dsc = input("설명 입력 : ")
            menu_dic[add_menu] =[category,price,dsc] # 추가 : 딕셔너리[키] = 값 새로운 키와 값을 추가
            for key in menu_dic: #메뉴가 추가됫는지 확인
                print(key, ":", menu_dic[key])
        else: print("메뉴가 이미 존재 합니다.")

    elif menu == "4":
        del_menu = input("삭제할 메뉴를 입력하세요 : ")
        if del_menu in menu_dic :
            del menu_dic[del_menu] # 삭제 : del 딕셔너리[키] 형식
            for key in menu_dic:  # 메뉴가 삭제됫는지 확인
                print(key, ":", menu_dic[key])
        else:
            print("삭제할 메뉴가 없습니다.")

    elif menu == "5":
        print("메뉴를 종료합니다 .")
        break
    else:
        print("선택 하신 메뉴가 없습니다 .")