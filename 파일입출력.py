#파일쓰기 : 파일을 읽거나 쓰기 위해서는 반드시 open() 해야함
#파일객체 = open(파일명, 파일모드, 인코등)
#파일명 : 파일경로 + 파일명 (파일경로를 입력하지 않으면 현재 위치에 저장)
#파일 모드: r(읽기),w(쓰기),a(추가, 파일이없으면 생성하고 추가,있으면 파일의 마지막에 추가)
# score_file = open("score.txt","w", encoding="utf-8")
# print("수학 : 50",file=score_file)
# print("영어 : 90",file=score_file)
#
# score_file.write("국어 : 70"+"\n")
# score_file.write("과학 : 40"+"\n")
# score_file.close()

#파일읽기
#read() : 파일내의 모든 내용을 하나의 문자열로 반환
#readline() : 해당 파일의 내용을 한 라인씩 읽어 문자열로 반환 , 더이상 읽을 내용이 없으면 None으로 반환
#readlines() : 해당 파일의 모든 라인을 순서대로 읽어 각각의 라인을 하나의 요소로 저장하는 트스트 반환
# score_file =open("score.txt","r",encoding="utf-8")
# print(score_file.read())
# score_file.close()
# while True :
#     line = score_file.readline() # 한줄 씩 읽어옴
#     if not line : break #더 이상 읽을 것이 없을때 None 값으로 확인되고 None은 거짓
#     print(line, end="") #한줄씩 읽기때문에 출바꿈 문자가 포함되어있음
# score_file.close()
# lines = score_file.readlines() # 해당 파일의 모든 라인을 순서대로 읽어 리스트 생성
# for e in lines :
#     print(e,end="")

# # with 키워드 사용하기 : open()이후에 자동으로 close를 호출해주는 기능
# with open("score.txt","r",encoding="utf-8") as score_file :
#     print(score_file.read())


# #피클  : 몰라도됨 이런게있다 이정도만 
# import pickle
#
# # # 객체를 직렬화하여 파일에 저장하기
# # data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# # with open('data.pickle', 'wb') as file:
# #     pickle.dump(data, file)
#
# # 파일에서 객체를 역직렬화하여 복원하기
# with open('data.pickle', 'rb') as file:
#     restored_data = pickle.load(file)
#
# print(restored_data)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}