# 숫자형

# 정수  : 123 , -123 , 0
# 실수  : 123.45 , -123.45 , 3 4e12
# 8진수 : 0o34 , 0o25 
# 16진수 : 0x2A , 0xFF

# ** 사칙 연산
# + : 더하기
# - : 빼기
# % : 나머지 연산
# / : 몫 연산
# \// <- // : 몫 중 정수만 반환 

# ** 문자열
# "Life"
# 'a'

# """Life
# is
# good"""

# '''Life
# is
# good'''

# ** 문자열 연산 
head = "hi"
tail = " python"
print(head + tail)

# ** 문자열 곱하기
a = "python"
a = a * 2
print(a)

# ** 문자열 길이 구하기
print(len(a))

# ** 문자열 인덱싱
print(a[3])
print(a[-1]) # 뒤 부터 시작

# ** 문자열 슬라이싱
print(a[0:4])
print(a[4:])
print(a[:5])

# ** 문자열 포매팅
# %s : 문자열
# %c : char
# %d : 정수
# %f : 실수
# %o : 8진수
# %x : 16진수
# %% : 문자 '%' 자체

print("hello %d world" %5)
print("hello %s world" %"안녕")
print("hello %d %% world" %95) # <- 95 % 로 나옴

# ** 포맷팅과 정렬 공백
print("%10s" %"안녕?") # 앞 10칸이 띄워짐
print("%-10s 입니다" %"안녕?") # 뒤 10칸이 띄워짐

# ** 소수점 표현하기
print("%10.4f" % 123456789011.1231561561) # 전체 길이가 10개인 문자열 공간에서 소수점 4자리까지 표현 > ????

# ** format 함수를 사용한 포매팅
print("apple {0} 개".format(3))
print("apple {0} 개가 {1}".format(3,"있습니다.")) # apple 3 개가 있습니다. <- 인덱스
print("apple {number} 개가 {string}".format(number = 3, string = "있습니다.")) # apple 3 개가 있습니다. <- 이름으로
print("apple {0} 개가 {string}".format(3, string = "있습니다.")) # apple 3 개가 있습니다. <- 인덱스와 이름 혼용

# ** format 함수 정렬
print("{0:<10} python".format("hi")) # 왼쪽 정렬 : hi         python
print("{0:>10} python".format("hi")) # 오른쪽 정렬 :        hi python
print("{0:^10} python".format("hi")) # 가운데 정렬 :     hi     python
print("{0:=^10} python".format("hi")) # 공백 채우기 : ====hi==== python
print("{0:!<10} python".format("hi")) # 공백 채우기 : hi!!!!!!!! python

# ** format 함수 소수점 표현
y = 3.1516546
print("{0:0.4f}".format(y)) # 소수점 4자리 까지 표현 : 3.1517
print("{0:10.4f}".format(y)) # 소수점 4자리 까지 표현 :     3.1517 <- 10칸 오른쪽으로 띄우기

# ** format 함수 문자 표현하기
print("{{and}}".format()) # {and}

# ** f 문자열 포매팅 : 파이썬 3.6 버전 부터 가능
name = '홍길동'
age = 30

print(f'나의 이름은 {name} 입니다. 나이는 {age} 입니다.')
print(f'나의 이름은 {name} 입니다. 나이는 {age + 10} 입니다.')

# ** f 문자열 포매팅 2번 딕셔너리 : 파이썬 3.6 버전 부터 가능
d = {'name' : "홍길동" , "age" : 30}
print(f'나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]} 입니다.')

# ** f 문자열 포매팅 3번 공백 채우기 : 파이썬 3.6 버전 부터 가능
print(f"{'hi':=^10}") # ====hi====
print(f"{'hi':!<10}") # hi!!!!!!!!

y = 3.1516165
print(f"{y:0.4f}") # 3.1516
print(f"{y:10.4f}") #     3.1516

print(f"{{and}}") # {and}

