# 입출력 함수

# 매개변수가 없는 함수
def say() :
  return "Hi"

# 매개변수가 잇는 함수
def add(a,b) :
  return a + b

# 결과 값이 없는 함수
def hi() :
  print("안녕")

# 여러개의 입력값을 받는 함수 만들기
def add_many(*args) :
  result = 0
  for i in args :
    result += i
    
  return result

# ** 매개변수를 지정하여 호출하기
result = add(b = 1, a = 1)

# ** 여러개의 입력값을 받는 함수
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


# * * * 키워드 파라미터 * * *
# 키워드 파라미터를 사용할 때는 매개변수 앞에 별 두 개(**)를 붙인다
def print_kwargs(**kwargs) :
  print(kwargs)
  
print_kwargs(name = 'foo' , age = 3) # {'name': 'foo', 'age': 3}


# * * * return 을 두개 이상이 가능하다!! * * *
# 밑의 함수는 더하기와 곱셈을 tuple 로 받을 수 있다!!
def add_and_mul (a , b) :
  return a+b , a*b

print(add_and_mul(1,2)) # (3, 2)

# * * * 매개변수에 초깃값 미리 설정 * * *
def say_myself(name , old, man = True) :
  if(man) :
    print(f"남자이고 이름은 {name} 이고, 나이는 {old} 입니다.")
  else :
    print(f"여자이고 이름은 {name} 이고, 나이는 {old} 입니다.")


#! 주의점
# def say_myself_exception(name , man = True , old) :
# 초기값은 c 언어와 마찬가지로 오른쪽 부터 시작한다.

# * * * 함수 안에서 선언한 변수의 효력 범위 * * *
def vartest (a) :
  a = "변경"

a = "일반"
vartest(a)
print(a) # 일반 <- 한마디로 상관이 없다

# 위와 같이 하고 싶다면 이렇게 바꾸어야 한다.
def vartest_change(a) :
  a = "변경"
  return a

a = "일반"
a = vartest_change(a)
print(a)

# ** global 함수
# 위와 같이 함수 내에서 전역변수 a 를 사용하고 싶을 때는 어떻해야 할까? (global 을 사용해 보자)
a = 1
def ab() :
  global a
  a = a + 3

ab()
print(a) # 4

# ** lambda 함수
# [lambda 매개변수1 , 매개변수2 , : 매개변수를 사용한 표현식]
lambda_add = lambda a , b : a+b
print(lambda_add(1,2))

lmb = lambda : print("a")
lmb()