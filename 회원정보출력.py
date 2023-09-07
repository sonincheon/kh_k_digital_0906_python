name = input("이름 :")
year = int(input("나이 :"))
gender = str(input("성별 : "))
job = int(input("1(학생), 2(회사원), 3(주부), 4(무직) :"))
jobs = ["", "학생", "회사원", "주부", "무직"]

if 0<year<200 :

    if gender == "m" or "M" :
        print("="*5 + "정보" + "="*5)
        print(f"이름 : {name}")
        print("성별 : 남자")
        print(f"나이 : {year}")
        print(f"직업 : {jobs[job]}")

    else:
        print("=" * 5 + "정보" + "=" * 5)
        print(f"이름 :{name}")
        print("성별 : 여자")
        print(f"나이 :{year}")
        print(f"직업 :{jobs[job]}")

else: print("나이를 다시 입력하세요 .")