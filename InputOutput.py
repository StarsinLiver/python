# 사용자 입력과 출력

# ** 사용자 입력함수
# a = input()
# print(a)

# ** print 한줄 출력
for i  in range(10) :
  print(i , end = ' ') # 0 1 2 3 4 5 6 7 8 9
  


# * * * * * 파일 입출력 * * * * *

# ** 파일 생성하기
# 파일 객체 = open(파일 이름 , 파일 열기 모드)
# r = 읽기 모드
# w = 쓰기 모드
# a = 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용
f = open("새파일1.txt" , 'w') # 쓰기
c = open("C:\\ALL_WORKSPACE\\1_STUDY\\04_pyton\\code1\\새파일2.txt" , 'w')

f.write("안녕하세요 여기는 f 객체 입니다.")
c.write('여기는 c 객체입니다.')

f.close()
c.close()

# * * * 파일 읽어 오기 * * *
# ** 1번 readline() 함수
# readline() 함수는 파일을 계속해서 한 줄씩 읽어 들일 수 있다.
f = open("새파일1.txt" , 'r') # r 읽어 오기
while True :
  line = f.readline()
  if not line : break
  print(line)

f.close()

# ** 2번. readlines() 함수
# readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다
# 이는 다음과 같다 ["문자열" , "문자열"]
f = open("새파일1.txt" , 'r') # r 읽어 오기
lines = f.readlines()
for line in lines :
  print(line)

f.close()

# ** 3번 read() 함수
# read() 함수는 파일의 내용 전체를 문자열로 돌려준다.
f = open("새파일1.txt" , 'r') # r 읽어 오기
data = f.read()

print(data)
f.close()



# * * * 파일에 새로운 내용 추가하기 * * *
# 추가모드 'a'를 사용하여 새로운 내용을 추가할 수 있다.
f = open("새파일1.txt" , 'a') # a 내용 추가하기
f.write("data 추가")

f.close()


# * * * with 문과 함께 사용하기
# 파일을 열면 항상 close 해 주는 것이 좋은데 다만 이렇게 파일을 열고 닫는 것을 자동으로 처리가 가능하다
with open("새파일3.txt" , 'w') as f :
  f.write("write with [with] grammar") 
  

