# 문자열 관련 함수
# ** 문자열 개수
a = "안녕하세요"
print(len(a)) # 5

# ** 해당 문자 개수 세기 (count)
a = "안녕녕하세요"
print(a.count('녕')) # 2

# ** 위치 알려주기 (find , index)
a = "Python is best choice"
print(a.find('b')) # 10
print(a.index('t')) # 2

# ** 문자열 삽입 : 각각 문자 사이에 , 삽입 (join)
a =  ",".join("abcd")
print(a) # a,b,c,d
print(",".join(['a','b','c','d'])) # a,b,c,d <- 배열에도 가능

# ** 소문자를 대문자로 바꾸기 (upper)
a = "hi"
print(a.upper()) # HI <- 깊은 복사

# ** 대문자를 소문자로 바꾸기
print(a.lower()) # hi <- 깊은 복사

# ** 공백 지우기 (lstrip : 왼쪽 공백 지우기 , rstrip : 오른쪽 공백 지우기 , strip : 양쪽 공백 지우기)

a = "       hi         a"  
print(a.lstrip()) # hi         a

a = "       hi    a     " 
print(a.rstrip()) #        hi    a

a = "        hi         "
print(a.strip()) # hi

# ** 문자열 바꾸기 (replace)
a = "Life is too short"
print(a.replace("Life" , "our time"))

# ** 문자열 나누기
a = "Life,is,too,short"
b = a.split(",")

print(b)


