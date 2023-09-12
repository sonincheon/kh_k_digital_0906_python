# ### [문제]
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# ### [입력]
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# ### [출력]
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
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


# 선생님 해답
def over_rate() :
    ls = list(map(int,input().split()))
    average = sum(ls[1:])/len(ls[1:])
    cnt = 0
    for i in range(1,len(ls)) :
        if ls[i] > average : cnt += 1
    return cnt/()

n = int(input())
rst = []
for i in range(n) :
    rst.append(aver_rate())

for e in rst :
    print(e)