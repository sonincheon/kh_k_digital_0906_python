file_name ="스타벅스일매출.txt"
f=open(file_name,"r",encoding="utf-8")
head = f.readline()      # 파일의 첫번쨰 줄을 읽음
head_list = head.split() # 메뉴명을 리스트화 시킴

espresso =[]
amricano = []
cafelatte =[]
capucino = []

for line in f : # f는 파일 객체이며 파일의 읽는 위치를 가리키는 식별자
    data_list =line.split() # 각각의 라인을 공백 기준으로 자름
    espresso.append(int(data_list[1]))
    amricano.append(int(data_list[2]))
    cafelatte.append(int(data_list[3]))
    capucino.append(int(data_list[4]))
f.close()

print(f"{head_list[1]} 전체 판매량 :{sum(espresso)}, 일평균 판매량 :{sum(espresso)/len(espresso)}")
print(f"{head_list[2]} 전체 판매량 :{sum(amricano)}, 일평균 판매량 :{sum(amricano)/len(amricano)}")
print(f"{head_list[3]} 전체 판매량 :{sum(cafelatte)}, 일평균 판매량 :{sum(cafelatte)/len(cafelatte)}")
print(f"{head_list[4]} 전체 판매량 :{sum(capucino)}, 일평균 판매량 :{sum(capucino)/len(capucino)}")




