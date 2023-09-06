#인덱싱과 슬라이싱

jumin ="901112-1234567"

gender =jumin[7] #성별
year = jumin[:2] #출생연도
month = jumin[2:4] #월
day = jumin[4:6] #일

print("생년월일 : " + jumin[:6])
print("뒷자리 :" + jumin[7:])
print("뒷자리 :" + jumin[-7:]) # 뒤부터는 -1 시작 예) [-1:] -> 7
