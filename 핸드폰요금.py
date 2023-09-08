# 영식 요금제 : 30초에 10원
# 민식 요금제 : 60초에 15원

n = int(input()) #통화 횟수
call = list(map(int, input().split())) #통화 횟수에 대한 통화시간
y_pay = m_pay = 0

for i in range(n):
    y_pay += (call[i] // 30) * 10 + 10    # // 몫을 구함
    m_pay += (call[i] // 60) * 15 + 15

if y_pay > m_pay:
    print("M", m_pay)
elif y_pay < m_pay:
    print("Y", y_pay)
else:
    print("Y M", y_pay)