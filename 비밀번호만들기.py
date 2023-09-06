# 각사이트 비밀번호 만들기
# 규칙1 : http://naver.com 앞의 http:// 잘라내기
# 규칙2 : 처음만난 점 이후 제거
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'o'갯수 + 글자에 포함된 'k'의 갯수 +"!"+자신의 이니셜
file_name = "password.txt"
fd = open(file_name, "wt")

while True:
    url = input("사이트: ")
    if url == 'exit': break
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")]  # 슬라이싱 : 처음부터 "."인덱스 미만 까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "sic"
    print("비밀번호 생성 : " + password)
    fd.write(password+"\n")

fd.close()
