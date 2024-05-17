# 집합 자료형 (set)

s1 = set([1,2,3])
print(s1)  # {1, 2, 3}

# 다음과 같이 문자열도 가능
s2  = set("hello")
print(s2) # {'o', 'e', 'l', 'h'}

# set 을 list 변환
s1 = set([1,2,3])
l1 = list(s1)
print(l1) # [1, 2, 3]

# set 을 튜플 변환
s1 = set([1,2,3])
t1 = tuple(s1)
print(t1) # (1, 2, 3)

# * * * 교집합 , 합집합 , 차집합 구하기 * * *
# ** 교집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

s3 = s1 & s2
print(s3) # {4, 5, 6}

s3 = s1.intersection(s2)
print(s3) # {4, 5, 6}

# ** 합집합
s3 = s1 | s2
print(s3) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

s3 = s1.union(s2)
print(s3) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# ** 차집합
s3 = s1 - s2
print(s3) # {1, 2, 3}

s4 = s2 - s1
print(s4) # {8, 9, 7}

s3 = s1.difference(s2)
print(s3) # {1, 2, 3}

s4 = s2.difference(s1)
print(s4) # {8, 9, 7}

# * * * 집합 자료형 관련 함수 * * *
# ** 값 1개 추가하기 (add)
s1 = set([1,2,3])
s1.add(4)
print(s1) # {1, 2, 3, 4}

# ** 값 여러개 추가하기 (update)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1) # {1, 2, 3, 4, 5, 6}

# ** 특정 값 제거하기
s1 = set([1,2,3])
s1.remove(2)
print(s1) # {1, 2, 3, 4, 5, 6}
