a = int(input("숫자 입력해주세요 :"))
b = int(input("숫자 입력해주세요 :"))
c = int(input("숫자 입력해주세요 :"))
sum_num = a * b * c
sum_num = str(sum_num)
a = [0, 0, 0, 0, 0, 0, 0, 0, 0]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
print(sum_num)
for i in range(0, sum_num.__len__()):
    for j in range(0, 9):
        if sum_num[i] == num[j]:
            a[j] += 1

for e in a:
    print(e)
