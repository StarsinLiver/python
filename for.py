# for 문

# ** 전형적인 for 문
test_list = [1,2,3]
for i in test_list : 
  print(i)
  
# ** 다양한 for 문의 사용
a = [(1,2,) , (3,4) , (5,6)]

for (first , last) in a :
  print(f"{first} , {last}")

# ** range 함수
# range() 함수는 숫자 리스트를 자동으로 만들어 준다.
a = range(10)
print(a) # range(0, 10)

# range(0,10) 이란?
# 이는 0,1,2,3,4,5,6,7,8,9,10 리스트를 만들어줌

for i in range(1,11) :
  print(i)
  

# * * * 리스트 내포 * * *
# ** [표현식 for 항목 in 반복 가능 객체 if 조건] ** 
# 리스트 안에 for문을 포함하는 리스트 내포(list comprehension)를 사용하면 좀 더 편리하고 직관적인 프로그램을 만들 수 있음

# ** 리스트 내포를 안 썼을 때
a = [1,2,3,4]
result = []

for num in a :
  result.append(num * 3)

print(result) # [3, 6, 9, 12]

# ** 리스트 내포를 사용했을 때
a = [1,2,3,4]
result = [num * 3 for num in a] # for 문을 돌려서 num * 3을 내포

print(result) # [3, 6, 9, 12]

# 또는 다음과 같이 사용할 수도 있다
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0] # if 문과 함께 사용
print(result) # [6, 12]


