# 리스트 자료형 == []
add = [1,2,3,4]

print(add[0])

# ** 파이썬 리스트는 아무거나 가능하다
add = [1 , 2 , 3 , [4,5,6] , [7,8,9]]

print(add[3][0]) # 4
print(add[-1][2]) # 9

# ** 리스트의 슬라이싱
a = [1,2,3,4]
b = a[0:2] # 문자열 슬라이싱과 비슷하다
print(b) 

c = a[:3]
print(c)

d = a[2:]
print(d)

# ** 리스트 더하기 연산 (+)
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c) # [1, 2, 3, 4, 5, 6]

# ** 리스트 반복하기 (*)
a = [1,2,3]
a = a * 3
print(a) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# ** 리스트 길이 구하기 (len)
print(len(a))

# ** 리스트 요소 추가 (append)
a = [1,2,3]
a.append(4)
print(a) # [1, 2, 3, 4]

a.append([5,6,7])
print(a) # [1, 2, 3, 4, [5, 6, 7]]

# ** 리스트 해당 인덱스에 요소 추가 (insert)
a = [1,2,3]
a.insert(0 , 4)
print(a) # [4, 1, 2, 3]

# ** 리스트 삭제 (del)
a = [1,2,3]
del a[1]
print(a) # [1, 3]

# ** 리스트 해당 요소 삭제 (remove)
a = [1,2,3]
a.remove(1)
print(a) # [2, 3]


# ** 리스트 정렬 (sort)
a = [1,4,5,2,6,3]
a.sort()
print(a) # [1, 2, 3, 4, 5, 6]

a = ['c' , 'b' , 'a']
a.sort()
print(a) # ['a', 'b', 'c']

# ** 리스트 뒤집기 (reverse)
a = [1,2,3,4,5]
a.reverse()
print(a) # [5, 4, 3, 2, 1]

a = ['a','b','c']
a.reverse()
print(a) # ['c', 'b', 'a']

# ** 위치 반환 (index)
a = [1,2,3]
print(a.index(2)) # 1

# ** 리스트 요소 끄집어내기 (pop)
a = [1,2,3]
b = a.pop()
print(a) # [1, 2]
print(b) # 3

# ** 리스트 요소 끄집어내기 (pop(x))
a = [1,2,3]
b = a.pop(1)
print(a) # [1, 3]
print(b) # 2

# ** 리스트에 포함된 요소 x의 개수 세기 (count)
a = [1,2,3,4,4,4]
print(a.count(4)) # 3