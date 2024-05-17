# if 문

# ** elif
if True : 
  print("true")
elif False : 
  print("true")
else :
  print('else')


# 비교 연산자
x = 1
y = 2

x > y
x < y
x == y
x != y
x >= y
x <= y

# ** and , or , not
# 다른 연산자로 and, or , not 이 있다

x or y  # x || y
x and y # x && y
not x   # !x

# ** in , not in 문법
# 파이썬은 다른 프로그래밍 언어에서 쉽게 볼 수 없는 재미있는 조건문을 제공
# 이는 true ,false 를 제공
l = [1,2,3]
t = (1,2,3)
x = 1

x in l      #  x in 리스트
x not in l

x in t      # x in 튜플
x not in t

x in "1"      # x in 문자열
x not in "1"

# ** in 문법 응용
pocket = ["paper" , "money"]
x = "money"
if x in pocket :
  print('주머니 안에 돈이 있습니다.')
else :
  print("주머니 안에 돈이 없습니다.")

