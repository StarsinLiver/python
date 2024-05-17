# 모듈
# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일이다 . 포듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 할 수 있다.

# * * * 예제 파일 - example/mod1.py * * *

# ** import 
# [ import 묘듈이름 ]
# 여기에서 모듈이름은  mod1.py 에서 .py 확장자를 제거한 mod1 만 가리킨다.

# 때로는 mod1.add  , mod1.sub 처럼 쓰지 않고 add , sub 처럼 사용하고 싶다면 이와 같이 가능하다
# [ from 묘듈이름 import 모듈 함수 ]

# 그런데 함수 둘다 사용하고 싶다면?
# [ from 묘듈이름 import * ]

# ** 프롬프트 예제
# PS C:\ALL_WORKSPACE\1_STUDY\04_pyton\code1> cd .\example\
# PS C:\ALL_WORKSPACE\1_STUDY\04_pyton\code1\example> python

# >>> import mod1
# add : 3
# sub : 4
# >>> print(mod1.add(1,2))
# 3



# * * * 예제파일 - example/mod2.py * * *
# ** 문제점
# 그런데 mod1 에서 print(add()) 와 print(sub()) 함수를 그대로 들고온다.
# 이를 방지 하기 위해서는 

# if __name == "__main__" :    을 사용해야 한다.
# if __name == "__main__" : 을 사용하면 __name__ == "__main__" 이 참이 되어 다음 문장을 수행하게된다. 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서
# 사용할 때는 __name__ == "__main__" 이 거짓이 되어 if 문 다음 문자장이 수행되지 않는다.

# ** 문제점 해결 프롬프트 예제
# >>> import mod2
# >>>

# ** __name__ 변수란 ?
# 파이썬의 __name__ 변수는 파이썬 내부적으로 사용하는 특별한 변수 이름이다. 



# * * * 예제파일 - example/mod3.py * * *
# ** 클래스나 변수등을 포함한 모듈

# >>> import mod3

# >>> print(mod3.PI) 
# 3.14592

# >>> a = mod3.Math()
# >>> print(a.solv(2))
# 12.58368

# >>> print(mod3.add(mod3.PI , 4.4))
# 7.545920000000001



# * * * 예제파일 - example/mod3.py * * *
# ** 그렇다면 해당파일에서 다른 모듈을 불러와보자

# ** 1번. 동일한 디렉터리에 있는 경우
import variable # 이와 같이 .py 확장자를 뺀 나머지로 가져오기가 가능



# ** 2번. 다른 디렉터리에 있는 경우
# ** 2-1 번. sys.path.append (모듈을 저장한 디렉터리) 사용하기
import sys

print(sys.path) # & C:/Users/san26/AppData/Local/Programs/Python/Python312/python.exe c:/ALL_WORKSPACE/1_STUDY/04_pyton/code1/module.py
# ['c:\\ALL_WORKSPACE\\1_STUDY\\04_pyton\\code1', 'C:\\Users\\san26\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip', 'C:\\Users\\san26\\AppData\\Local\\Programs\\Python\\Python312\\DLLs', 'C:\\Users\\san26\\AppData\\Local\\Programs\\Python\\Python312\\Lib', 'C:\\Users\\san26\\AppData\\Local\\Programs\\Python\\Python312', 'C:\\Users\\san26\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages']

sys.path.append("C:\\ALL_WORKSPACE\\1_STUDY\\04_pyton\\code1\\example") # 해당 디렉터리 사용하겠음

import mod3
print (mod3.add(1,2)) # 3

# ** 2-2 번. PYTHONPATH 환경변수 사용하기 -- package 와 관련있습니다. package.py 를 참조하세요!!!
# 환경변수 등록 

# C:\ALL_WORKSPACE\1_STUDY\04_pyton\code1\example> set PYTHONPATH=C:\\ALL_WORKSPACE\\1_STUDY\\04_pyton\\code1\\example
# PS C:\ALL_WORKSPACE\1_STUDY\04_pyton\code1\example> python

# >>> import mod3
# >>> print(mod3.add(1,2))
# 3