# 라이브러리

# * * * sys * * *
# sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 도와주는 모듈이다.

# ** 1번. sys.argv 리스트에 값 추가
# 명령어 : python .\library.py abc pey guido

import sys
print(sys.argv)

# C:\ALL_WORKSPACE\1_STUDY\04_pyton\code1> python library.py abc pey guido  
# ['library.py', 'abc', 'pey', 'guido']

# ** 2번. 강제로 스크립트 종료하기 - sys.exit
# sys.exit() 

# ** 3번 자신이 만든 모듈 불러와 사용하기 = sys.path
# sys.path는 파이썬 모듈들이 저장되어 있는 위치를 나타낸다. 즉 이 위치에 있는 파있너 모듈은 경로에 상관없이 어디에서나 불러올 수 있다.

print(sys.path) # ['c:\\ALL_WORKSPACE\\1_STUDY\\04_pyton\\code1', ... ]

# * * * pickle * * *
# pickle 은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
# 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data 를 그대로 파일에 저장하는 방법을 보여준다.
import pickle

# ** 1번 dump
f = open("test.txt" , 'wb') # b 는 바이너리 데이터
data = {1 : 'python' , 2 : 'you need'}
pickle.dump(data ,f)
f.close()

# ** 2번 load
# 다음은 pickle.dump로 저장한 파일은 pickle.load()를 사용해서 원래 있던 딕셔너리 객체 (data) 상태 그대로 불러오는 예이다.
f = open("test.txt" , 'rb')
data = pickle.load(f)
print(data) # {1: 'python', 2: 'you need'}


# * * * OS * * * 
# OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.

# ** 1. 내 시스템 환경 변수 값을 알고 싶을 때 - os.environ
import os

print(os.environ)

# 다음과 같이 호출이 가능하다
print(os.environ['PATH'])

# ** 2. 디렉터리 위치 변경하기 - os.chdir
# 현재 디렉터리 위치를 변경할 수 있다.
# os.chdir("C:\\Windows")

# ** 3. 디렉터리 위치 돌려받기 - os.getcwd
# os.getcwd는 현재 자신의 디렉터리 위치를 돌려준다.
a = os.getcwd()

print(a)

# ** 4. 시스템 명령어 호출하기 - os.system
# 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다.
# os.system("명령어")처럼 사용한다.

os.system("ipconfig")

# ** 5. 실행한 시스템 명령어의 결과값 돌려받기 - os.popen
# op.popen은 시스템 명령어를 실행한 결과값을 읽기 모드의 형태의 파일 객체로 돌려준다.
f = os.popen("dir") # 해당 디렉터리의 파일들 보여주기
print(f.read())

# ** 6. 디렉터리 생성   - os.mkdir(디렉터리)
# ** 7. 디렉터리 삭제   - os.rmdir(디렉터리)
# ** 8. 파일 삭제       - os.unlink(파일 이름)
# ** 9. 파일 이름 교체  - os.rename(src , dst) src를 dst 로 이름 교체


# * * * shutil * * *
# shutil 은 파일을 복사해 주는 파이썬 모듈이다.
# 다음의 예시는 src라는 이름의 파일을 dst로 복사한다 만약 dst가 디렉터리 이름이라면 src라는 파일 이름으로 dst 디렉터리에 복사하고 동일한 파일 이름이 있을 경우에는 
# 덮어쓴다
import shutil
shutil.copy("src.txt" , "dst.txt")


# * * * glob * * *
# 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름을 모두 알아야 할 때가 있는데 이럴때 glob 모듈을 사용한다.
# ** 1. 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)
# glob 모듈은 디렉터리 안의 파일들을 읽어서 돌려준다 *,? 등 메타 문자를 써서 원하는 파일만 읽어 들일 수도 잇다

# 해당 디렉터리의 mark 로 시작하는 파일을 모두 찾아서 읽어들이기
import glob

a = glob.glob("C:\\ALL_WORKSPACE\\1_STUDY\\04_pyton\\code1")
print(a) #  배열로 파일 위치를 문자열로 반환


# * * * tempfile * * *
# 파일을 임시로 만들어서 사용할 때 유용한 모듈이다. 

# ** 1. tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
import tempfile
filename = tempfile.mkstemp()
print(filename)

# ** 2. tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다.
# 이 파일은 기본적으로 바이너리 쓰기 모드 (wb)를 갖는다
f = tempfile.TemporaryFile()
f.close()


# * * * time * * *
# 시간과 관련된 time 묘듈이다.

# ** 1. time.time
# time.time()은 UTC(Universal Time Coordinated 협정 세계 표준시)를 사용하여 현재 시간을 돌려준다.
import time
t = time.time()
print(t)

# ** 2. time.localtime
# time.localtime 은 time.time()이 돌려준 실수 값을 사용하여 연도 , 월 , 일 , 시 , 분 초, .. 의 형태로 바꾸어 주는 함수이다.
t = time.localtime(time.time())
print(t)

# ** 3. time.asctime
# 위 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.
t = time.asctime(time.localtime(time.time()))
print(t)

# ** 4. time.ctime
# time.asctime(time.localtime(time.time())) 은 time.ctime()을 사용해 간편하게 표시할 수 있다.
# asctime 과 다른 점은 ctime 은 항상 현재 시간만 돌려준다는 점이다,
t = time.ctime()
print(t)

# ** 5. time.strtime('출력할 형식 포맷 코드' , time.localtime(time.time()))
# time.strtime 함수는 함수 시간에 관계된 것을 세밀하게 표현하는 여러가지 포맷 코드는 제공한다.

# %a : 요일 줄임말                         : Mon
# %A : 요일                                : Monday
# %b : 달의 줄임말                         : Jan
# %B : 달                                  : January
# %c : 날짜와 시간                         : 06/01/01 17:22:31
# %d : 날(day)                             : [01,31]
# %H : 24시간 출력                         : [00,23]
# %l : 12시간 출력                         : [01,12]
# %j : 1년 중 누적 날짜                    : [001,366]
# %m : 달                                  : [01,12]
# %M : 분                                  : [01,59]
# %p : AM or PM                            : AM
# %S : 초                                  : [00,59]
# %U : 1년중 누적 주                       : 일요일 시작 : [00,53]
# %w : 숫자로 된 요일                      : [0(일요일) , 6]
# %W : 1년 중 누적 주-월요일을 시작으로    : [00,53]
# %x : 현재 설정된 지역에 기반한 날짜 출력 : [06/01/01]
# %X : 현재 설정된 지역에 기반한 시간 출력 : 17:22:21
# %Y : 연도 출력                           : 2001
# %Z : 시간대 출력                         : 대한민국 표준시
# %% : 문자                                : %
# %y : 세기 부분을 제외한 연도 출력        : 01

# ** 6. time.sleep
# time.sleep 함수는 주로 루프 안에서 많이 사용한다. 이 함수를 사용하면 일정 시간 간격을 두고 루프를 실행할 수 있다.
time.sleep(1)


# * * * calendar * * *
# calendar 는 파이썬에서 달력을 볼 수 있게 해주는 모듈이다.
import calendar

# ** 1. calendar.calendar(연도)를 사용하면 그해의 전체 달력을 볼 수 있다.
calendar.calendar(2002)

# ** 2. calendar.prcal(연도)를 사용해도 똑같은 결과를얻는다.
calendar.prcal(2002)

# ** 3. 해당 달력만 보여주는 calendar.prmonth(연도 , 달)
calendar.prmonth(2015, 12)

# ** 4. calendar.weekday
# weekday(연도 , 월 , 일) 함수는 그 날짜에 해당하는 요일 정보를 돌려준다.
# 0 은 월요일 부터 6 일요일 이라는 값을 준다.
calendar.weekday(2015, 12 , 31)

# ** 5. calendar.mothrange
# monthrange(연도 , 월) 함수는 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 잇는 지를 튜플 형태로 돌려준다.
calendar.monthrange(2015 , 12) # (1 , 31)


# * * * random * * *
# 난수를 발생시키는 모듈이다.

# ** 1번 난수
import random
random.random() # 0.45461651648

# ** 2번. 정수
random.randint(1 , 10) # 1 ~ 10

# ** 3번 random_pop
# random_pop 함수는 리스트의 요소중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 돌려준다.
# 물론 꺼낸 요소는 pop 메서드에 의해 사라진다.
def random_pop(data) : 
  number = random.choice(data)
  data.remove(number)
  return number

# ** 4번 random.choice(data)
# random.choice 함수는 입력으로 받은 리스트에서 무작위로 하나를 선택하여 돌려준다.
data = [1,2,3]
random.choice(data)

# ** 5. random.shuffle
# 리스트의 항목을 무작위로 섞는다.
data = [1,2,3]
random.shuffle(data)


# * * * webbrowser * * *
# webbrowser 은 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다. 해당 url 로 향하게 가능하다.

import webbrowser

# ** 1. 웹 브라우저 실행 후 url 이동
webbrowser.open("http://google.com")

# ** 2. 새로운 웹 브라우저 실행
webbrowser.open_new("http://google.com")

# ** 3. 새로운 탭 실행
webbrowser.open_new_tab("http://google.com")


# * * * treading * * *
# 쓰레드를 다루는 모듈이다.
# 2가지 이상의 일을 동시에 실행하는 것이 가능하다.
import threading

# ** 1번 쓰레드 만들기
def long_task() :
  for i in range(4) :
    print(i)


t = threading.Thread(target = long_task)

# ** 2. start 
# 쓰레드 실행
t.start()

# ** 3. join
# 쓰레드의 join 함수는 해당 스레드가 종료될 때까지 기다리게 한다.
t.join()