# 집합이란 ? 주로 중복 제거를 목적으로 자주 사용 됩니다 .
# 순서가 보장 되지 않음
# 중복 불가
# mutable 특성을 가짐
s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

#중복 제거
s3 = set([1,2,3,4,5,1,2,3,4,5,1,2,3])
print(s3)

# 합집합
print(s1.union(s2)) # .union(합칠집합) 중복 제거됨
print(s1 | s2) # 합집합 중복제거됨

#교집합
print(s1.intersection(s2)) # .intersection 같은것만 표시됨 (교집합)
print(s1&s2)

#차집합
print(s1.difference(s2)) # s1- s2 로 s1집합에 s2집합에포함된 요소들만 제거
print(s1-s2)

import random
nums = set()
while True :
    num = random.randrange(1,46)
    nums.add(num)
    if len(nums) == 6: break
print(nums)
