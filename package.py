# 패키지란 무엇인가?
# 패키지(Packages) 는 도트(.) 를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다. 예를 들어 모듈 이름이 A,B 인 경우 
# A는 패키지 이름이 되고 B는 A 패키지의 모듈이 된다.

# ** 예제 패캐지
# game
#  ┣ graphic
#  ┃ ┣ render.py
#  ┃ ┗ __init__.py
#  ┣ sound
#  ┃ ┗ echo.py
#  ┗ __init__.py

# ** 명령 프롬프트로 해당 game 패키지를 참조할 수 있도록 set 명령어로 환경변수를 추가한다.
# PS C:\ALL_WORKSPACE\1_STUDY\04_pyton\code1> set PYTHONPATH=C:\ALL_WORKSPACE\1_STUDY\04_pyton\code1 

import example.game.sound.echo
example.game.sound.echo.echo_test() # echo


# * * * __init__.py 의 용도 * * *
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
# 만약 game , sound , graphic 등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.

# 다음을 보자

# 패키지
#  ┣ sound
#  ┃ ┗ echo.py

# >>> from example.game.sound import *
# >>> echo.echo_test()
#! Traceback (most recent call last):
#! File "<stdin>", line 1, in <module>
#! NameError: name 'echo' is not defined <- 에러

# * * * 해결법 
# 이렇게 특정 디렉터리의 모듈을 *를 사용하여 import 할 때에는 다음과 같이 해당 디렉터리의 __init__.py 파일에 __all__ 변수를 설정하고 import 할 수 있는 모듈을 정의해 주어야한다.

# 패키지 
# sound
#  ┣ echo.py
#  ┗ __init__.py

# C:\ALL_WORKSPACE\1_STUDY\04_pyton\code1\example\game\sound\__init__.py
# __all__ = ['echo']


# * * * relative 패키지 * * *
# 만약 graphic 디렉터리의 render.py 모듈이 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면?

# C:\ALL_WORKSPACE\1_STUDY\04_pyton\code1\example\game\graphic\render.py
# from example.game.sound.echo import echo_test
# echo_test() 함수 호출

# 명령 프롬프트 (python)
# >>> from example.game.graphic.render import render_test
# >>> render_test()
# render
# echo

# ** 위의 힘듦을 다음과 같이 import 가능하다.
# C:\ALL_WORKSPACE\1_STUDY\04_pyton\code1\example\game\graphic\render.py
# [ from ..sound.echo import echo_test ]
# echo_test() 함수 호출

# 여기에서 .. 은 부모 디렉터리를 의미한다. graphic 과 sound 디렉터리는 동일한 깊이 (depth) 이므로 부모 디렉터리(..) 을 사용하여 위와 같은 import 가 가능하다.