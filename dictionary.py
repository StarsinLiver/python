# 딕셔너리 자료형 (Map 구조)

# ** 딕셔너리 쌍 추가 , 삭제
a = {1 : 'a'}
a[2] = 'b'

print(a) # {1: 'a', 2: 'b'}

a['name'] = 'pey'

print(a) # {1: 'a', 2: 'b', 'name': 'pey'}

# ** 딕셔너리 요소 삭제하기
del a[1] # key 가 1인 것 삭제

# ** 딕셔너리에서 key 를 사용해 value 얻기
grade = {'pey' : 10 , 'juliet' : 99}
peyNumber = grade['pey']
julietNumber = grade['juliet']

print(peyNumber)
print(julietNumber)

# * * * 딕셔너리 관련 함수 * * * 

# ** key 리스트 만들기
a = {'name' : 'pey' , 'phone' : '102035531651' , 'birth' : '1110'}
b = a.keys() # dict_keys 라는 객체를 만듦
print(b) # dict_keys(['name', 'phone', 'birth'])

# 다음과 같이 활용 가능
for k in a.keys() :
  print(k)


# dict_keys 객체를 리스트로 변환
c = list(a.keys())
print(c) # ['name', 'phone', 'birth']

# ** value 리스트 만들기
a.values() # dict_values 객체를 만듦 - 나머지 위와 동일 

# ** key , value 쌍 얻기
b = a.items()
print(list(b)) # dict_items - key value 쌍을 튜플로 묶을 값 반환 [('name', 'pey'), ('phone', '102035531651'), ('birth', '1110')]

# ** key , value 쌍 모두 지우기
a.clear()

# ** key로 value 얻기 (get)
name = a.get('name')

# ** 해당 key 가 딕셔너리 안에 있는지 조사하기 (in)
a = {'name' : 'pey' , 'phone' : '102035531651' , 'birth' : '1110'}
print ('name' in a) # true
print ('email' in a) # false
