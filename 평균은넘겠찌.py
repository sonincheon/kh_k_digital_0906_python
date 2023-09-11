case = int(input("케이스의 갯수 : "))
score = list(map(int,input(f"{case}명의 학생들의 점수 : ").split()))
sum = 0;
for e in score :
    sum += e
cnt=[]
if len(score) == case :
    for e in score :
        if (sum/case)<e :
            cnt.append(e)
else: print("입력하신 케이스수와 점수가 맞지않습니다.")

print(f"{(len(cnt)/case * 100):0.3f}%")
