# 회원정보 출력하기 (1단계는 현재 상태대로 -> 함수형태로)
# jobs = ["", "학생", "회사원", "주부", "무직"]
# jobs_str = "", "학생", "회사원", "주부", "무직" # 튜플

def input_age() :
    while True :
        age = int(input("나이 : "))
        return age
        if not (0 < year < 200):
            print("나이를 다시 입력하세요 .")


def input_gender() :
    while True:
        gender = input("성별 : ")
        if gender == 'm' or 'M' :  return"남성"
        elif gender == 'f' or 'F' :  return"여성"
        print("성별을 다시 입력하세요. ")

def input_job() :
    while True:
        job = int(input("1(학생), 2(회사원), 3(주부), 4(무직) : "))
        if (0 < job < 5): return job
        else: print("직업을 다시 입력하세요. ")

def print_info(name,age,gender,job) :
    jobs = ["", "학생", "회사원", "주부", "무직"]
    print("=" * 5 + "정보" + "=" * 5)
    print(f"이름 : {name}")
    print(f"성별 : {gender}")
    print(f"나이 : {age}")
    print(f"직업 : {jobs[job]}")
    print("=" * 13)
    return f"이름 :{name}\n나이 :{age}\n성별: {gender}\n직업: {jobs[job]}"

member_info = "member.txt"
fd = open(member_info,"wt",encoding="utf-8")

while True :
    name = input("이름 : (종료 하려면 quit)")
    if name == 'quit' : break
    age = input_age()
    gender = input_gender()
    job = input_job()
    rst = print_info(name,age,gender,job)
    fd.write(rst + "\n")
fd.close()





# name = input("이름 : ")
# while True :
#     year = int(input("나이 : "))
#     if not (0 < year < 200):
#         print("나이를 다시 입력하세요 .")
#     else:
#         break
# while True :
#     gender = input("성별 : ")
#     if not(gender == 'm'or'M'or'w'or'W' ) :
#         print("성별을 다시 입력하세요. ")
#     else:
#         break
# while True :
#     job = int(input("1(학생), 2(회사원), 3(주부), 4(무직) : "))
#     if not(0<job<5) :
#         print("직업을 다시 입력하세요. ")
#     else:
#         break
#
# if gender == 'm' or 'M' : gen_str ="남성"
# else: gen_str ="여성"
#
# print("="*5 + "정보" + "="*5)
# print(f"이름 : {name}")
# print(f"성별 : {gen_str}")
# print(f"나이 : {year}")
# print(f"직업 : {jobs[job]}")


