# 예외 처리

# ** 오류 예외 처리 기법
# try :
  # except [발생 오류 [as 오류 메시지 변수]] :
  
# ** 1번 try except 만 사용
try :
  4 / 0
except :
  print("오류")

# ** 2번 발생 오류만 포함한 except 문
try :
  4 / 0
except ZeroDivisionError :
  print("zeroDivisionError")

# ** 3번 발생 오류와 오류 메시지 변수까지 포함한 except 문
try :
  4 / 0
except ZeroDivisionError as e:
  print(e)

# * * * try ~ except ~ finally * * *
try : 
  a = [1,2]
  print(a[3])
  4/0
except (ZeroDivisionError , IndexError) as e :
  print(e)
finally :
  pass


# * * * 오류 회피하기 pass * * *
try :
  print()
except :
  pass


# * * * 오류 일부러 발생시키기 (raise) * * *
class Bird:
  def fly(self) :
    raise NotImplementedError
  
class Eagle(Bird) :
  pass

eagle = Eagle()
try :
  eagle.fly()
except NotImplementedError as e :
  print(e)
finally :
  print("try ~ catch 종료")


# * * * 예외 만들기 * * *
# Exception 클래스를 상속하여 만들수 있다.
class MyError (Exception) :
  def __str__ (self) :
    return "허용되지 않는 벌명입니다."

def say_nick (nick) : 
  if nick == '바보' :
    raise MyError()
  print(nick)

try :
  say_nick("바보")
except MyError as e : 
  print(e)

