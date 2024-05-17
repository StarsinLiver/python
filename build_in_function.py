# 내장 함수

# ** 절대값 [ abs(x) ]
a = abs(-3)

# ** all(x) 
# 반복 가능한 (iterable) 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True , 거짓이 하나라도 있으면 False 를 돌려준다 
t = all([1,2,3])
print(t)

# ** any 
# any(x) 는 x 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False 를 돌려준다. all(x) 의 반대이다.
t = any([1,2,3,0])
print(t)

f = any([0,""])
print(f)

# ** chr 
# chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
a = chr(97)
print(a) # a

b = chr(48)
print(b) # 0

# ** dir
# dir은 객체가 자체적으로 가지고 잇는 변수나 함수를 보여준다. 다음 예는 리스트와 딕셔너리 객체 관련 함수(메서드)를 보여주는 예이다.
a = dir([1,2,3])
print(a)

b = dir({'1' : 'a'})
print(b)

# ** divmod
# divmod(a,b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
a = divmod(7,3)
print(a) # (2, 1)

# ** enumerate 
# '열거하다' 라는 뜻이다. 이 함수는 순서가 있는 자료형 (리스트 , 튜플 , 문자열) 을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
for i , name in enumerate(['body' , 'foo' , 'bar']) : 
  print(i , name)

# 0 body
# 1 foo
# 2 bar

# ** eval(expression)
# eval(expression)은 실행 가능한 문자열 (1+2 , 'hi' + 'a'같은 것)을 입력으로 받아 문자열을 실행한 결과값을 도려주는 함수이다.
a = eval('1+2')
print(a) # 3

b = eval("'hi' + 'a'")
print(b) # hia

c = eval('divmod(4,3)')
print(c) # (1, 1)

# ** filter
# filter 함수는 첫 번째 인수로 함수 이름을, 두번째 인수로 그 함수로 차례로 들어갈 반복 가능한 자료형을 받는다.
# 그리고 두 번째 인수인 박복 가능한 자료형 요소가 첫번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.

def positive(x) :
  return x > 0

print(list(filter(positive , [1 , -3 , 2 , 0 , -5 , 6]))) # [1, 2, 6]

print(list(filter(lambda x : x > 0  , [1,-3,2,0,-5,6]))) # [1, 2, 6]

# ** hex
# hex(x) 는 정수 값을 입력받아 16진수(hexadecimal) 로 변환하여 돌려주는 함수
a = hex(234)
print(a) # 0xea

b = hex(3)
print(b) # 0x3

# ** id
# id(object) 는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.
id(3)

# ** input
# input([prompt]) 은 사용자 입력을 받는 함수이다.
# 매개변수로 문자열을 주면 다음 세 번째 예에서 볼 수 있듯이 그 문자열은 프롬프트가 된다.
a = input()
print(a)

# ** int 
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그래도 돌려준다.
a = int('3')
print(a) # 3

b = int(3.4)
print(b) # 3

c = int('11' , 2) # 2진수로 표현
print(b) # 3

d = int('1A' , 16)
print(b) # 26

# ** isinstance
# isinstance(object , class) 는 첫번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True , 거짓이면 False를 돌려준다
class Person : pass

a = Person()
t = isinstance(a , Person)
print(t) # True

# ** len
# len(s) 은 입력값 s의 길이 (요소의 전체 개수)를 돌려주는 함수
a = len('python')
print(a)

b = len([1,2,3])
print(b)

c = len((1, 'a'))
print(c)

# ** list
# list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
a = list("python")
print(a) # ['p', 'y', 't', 'h', 'o', 'n']

b = list((1,2,3))
print(b) # [1, 2, 3]

# ** map
# map(f , iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
def two_times(x) : return x * 2

a = list(map(two_times , [1,2,3,4]))
print(a) # [2, 4, 6, 8]

# lambda 사용
a = list(map(lambda x : x * 2 , [1,2,3,4]))
print(a) # [2, 4, 6, 8]


# ** max
# max(iterable)는 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수이다.
a = max([1,2,3])
print(a) # 3

b = max('python')
print(b) # y

# ** min
# min(iterable)는 max 함수의 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수이다.
a = min([1,2,3])
print(a) # 1

b = min('python')
print(b) # h

# ** oct
# oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
a = oct(34)
print(a) # 0o42

# ** open 
# open(filename , [mode])은 '파일이름'과 '읽기방법'을 입력받아 파일객체를 돌려주는 함수이다. 읽기 방법 (mode)를 생략하면 기본값인 읽기 전용 모드(r)로
# 파일 객체를 만들어 준다 
# 해당 예제는 InputOutput.py를 참조하자

# ** ord
# ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.
a = ord('a')
print(a) # 97

# ** pow 
# pow(x,y)는 x의 y를 제곱한 결괏값을 돌려주는 함수이다.
a = pow(2,4)
print(a) # 16

# ** range
# range([start,] , stop [,step])는 for 문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복가능한 객체로 만들어 돌려준다.
# 인수가 3개일 경우를 보자
a = list(range(1 , 10 , 2))
print(a) # [1, 3, 5, 7, 9]

# ** round
# round(number [,ndigits]) 함수는 숫자를 입력받아 반올림 해주는 함수이다.
a = round(4.6)
print(a) # 5

b = round(5.6789,2) 
print(b) # 5.68

# ** sorted
# sorted(iterable) 함수는 입력값을 정렬한후 그 결과를 리스트로 돌려주는 함수이다
a = sorted([3,1,2])
print(a)

# ** str
# str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수이다.
a = str(3)
print(a) # '3'

# ** sum(iterable) 은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.
a = sum([1,2,3])
print(a) # 6

# ** tuple
# tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다
# 만약 튜플이 입력으로 들어오면 그대로 돌려준다
a = tuple("abc")
print(a) # ('a', 'b', 'c')

# ** type
# type(object)은 입력값의 자료형이 무엇인지 알려주는 함수이다.
a = type("abc")
print(a) # <class 'str'>

# ** zip
# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
# 여기서의 iterable은 반복 가능한 자료형 여러개를 입력할 수 있다는 뜻이다.
a = list(zip([1,2,3] , [4,5,6]))
print(a) # [(1, 4), (2, 5), (3, 6)]

b = list(zip("abc" , "def"))
print(b) # [('a', 'd'), ('b', 'e'), ('c', 'f')]





